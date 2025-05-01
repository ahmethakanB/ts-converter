import os
from pathlib import Path
import pkgutil
import inspect
import json
from importlib import import_module

from django.core.exceptions import ImproperlyConfigured
from rest_framework import serializers
from rest_framework.serializers import (
    BaseSerializer,
    ListSerializer,
    Serializer as DRFSerializer,
    ModelSerializer,
)
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField

from attributes.tables import BaseTableDto
from attributes.forms import BaseFormDto

MODES = ("create", "update", "view")
SERIALIZER_PACKAGE = "core.api.serializers"

def _type_code_for_field(field: serializers.Field) -> int:
    mapping = {
        serializers.IntegerField: 9,
        serializers.CharField: 18,
        serializers.BooleanField: 3,
        serializers.DateTimeField: 16,
        serializers.DecimalField: 15,
    }
    for cls, code in mapping.items():
        if isinstance(field, cls):
            return code
    return 1

TYPE_CODE_TS_MAP = {
    1: "any",
    3: "boolean",
    9: "number",
    15: "number",
    16: "string",
    18: "string",
}

def _ts_type_for_field(field: serializers.Field) -> str:
    many = getattr(field, "many", False)
    if isinstance(field, PrimaryKeyRelatedField):
        return "number[]" if many else "number"
    if isinstance(field, SlugRelatedField):
        return "string[]" if many else "string"
    if isinstance(field, ListSerializer):
        child_type = _ts_type_for_field(field.child)
        return f"{child_type}[]"
    if isinstance(field, DRFSerializer) and not isinstance(field, ModelSerializer):
        return f"{field.__class__.__name__}Dto"
    code = _type_code_for_field(field)
    return TYPE_CODE_TS_MAP.get(code, "any")

def export_serializer(serializer: BaseSerializer) -> str:
    name = serializer.__class__.__name__
    lines = [f"export interface {name} {{"]
    for field_name, field in serializer.get_fields().items():
        ts_type = _ts_type_for_field(field)
        optional = "?" if not getattr(field, "required", False) else ""
        lines.append(f"  {field_name}{optional}: {ts_type};")
    lines.append("}")
    return "\n".join(lines)

def export_serializers() -> list[str]:
    sections = []
    try:
        pkg = import_module(SERIALIZER_PACKAGE)
    except ModuleNotFoundError:
        return sections

    if hasattr(pkg, "__path__"):
        module_names = [SERIALIZER_PACKAGE] + [
            name for _, name, _ in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + ".")
        ]
    else:
        module_names = [SERIALIZER_PACKAGE]

    for mod_name in module_names:
        try:
            module = import_module(mod_name)
        except ModuleNotFoundError:
            continue
        for attr in dir(module):
            cls = getattr(module, attr)
            if (
                inspect.isclass(cls)
                and issubclass(cls, BaseSerializer)
                and cls is not BaseSerializer
            ):
                if not hasattr(cls, "Meta"):
                    print(f"⚠️ Skipping {cls.__name__}: missing Meta")
                    continue
                try:
                    inst = cls()
                    sections.append(export_serializer(inst))
                except Exception as e:
                    print(f"⚠️ Skipping {cls.__name__}: {e}")
    return sections

def export_table_dtos() -> list[str]:
    sections = []
    mod = import_module("attributes.tables")
    for name, cls in inspect.getmembers(mod, inspect.isclass):
        if issubclass(cls, BaseTableDto) and cls is not BaseTableDto:
            data = cls.column_config()
            const = json.dumps(data, ensure_ascii=False, indent=2)
            sections.append(f"export const {name}Columns: Column[] = {const};")
    return sections

def export_form_dtos() -> list[str]:
    sections = []
    mod = import_module("attributes.forms")
    for name, cls in inspect.getmembers(mod, inspect.isclass):
        if not issubclass(cls, BaseFormDto) or cls is BaseFormDto:
            continue
        for mode in MODES:
            raw = cls.form_config(mode=mode)
            configs = raw if isinstance(raw, list) else [raw]
            for cfg in configs:
                title = cfg.pop("title", None)
                if title is not None:
                    cfg["label"] = title
                input_type = cfg.get("formAttributes", {}).get("inputType")
                cfg["type"] = str(input_type) if input_type is not None else "text"
            const = json.dumps(configs, ensure_ascii=False, indent=2)
            sections.append(f"export const {name}_{mode}_Fields: FormField[] = {const};")
    return sections

def export_all_ts(target: Path):
    if not isinstance(target, Path):
        target = Path(target)
    sections = [
        "// AUTO-GENERATED – do not edit by hand",
        """
export interface Column {
  field: string;
  title: string;
  hidden?: boolean;
  typeCode?: number;
  tableAttributes?: { [key: string]: any };
  [key: string]: any;
}

export interface FormField {
  field: string;
  label: string;
  type: string;
  required?: boolean;
  disabled?: boolean;
  formAttributes?: { [key: string]: any };
  [key: string]: any;
}
""",
    ]
    sections.extend(export_serializers())
    sections.extend(export_table_dtos())
    sections.extend(export_form_dtos())
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        target.write_text("\n\n".join(sections), encoding="utf-8")
    except Exception as exc:
        raise ImproperlyConfigured(f"columns.ts üretilemedi: {exc}") from exc
    print(f"✅ Generated TS types at {target}")

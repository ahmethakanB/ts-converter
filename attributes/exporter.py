import pkgutil
import inspect
import json
from pathlib import Path
from importlib import import_module

from django.apps import apps as django_apps
from django.db import models as django_models
from django.urls import URLPattern, URLResolver
from rest_framework import serializers
from rest_framework.serializers import (
    BaseSerializer, ListSerializer,
    Serializer as DRFSerializer, ModelSerializer
)
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField
from rest_framework.views import APIView

from attributes.tables import BaseTableDto
from attributes.forms import BaseFormDto

# ————— Constants —————
MODES = ("create", "update", "view")
SERIALIZER_PACKAGE = "core.api.serializers"
OUTPUT_DIR = Path("templates/ts_converter")

CORE_INTERFACES = {
    "Column": {
        "field": "string",
        "title": "string",
        "hidden?": "boolean",
        "typeCode?": "number",
        "tableAttributes?": "{ [key: string]: any }",
        "[key: string]": "any",
    },
    "FormField": {
        "field": "string",
        "label": "string",
        "type": "string",
        "required?": "boolean",
        "disabled?": "boolean",
        "formAttributes?": "{ [key: string]: any }",
        "[key: string]": "any",
        "api?": "any",
        "model_name?": "string",
        "model?": "string",
        "serializer?": "string",
    },
}


def export_core_interfaces() -> list[str]:
    lines = ["// AUTO-GENERATED – Core Interfaces"]
    for iface, props in CORE_INTERFACES.items():
        lines.append(f"export interface {iface} {{")
        for name, t in props.items():
            lines.append(f"  {name}: {t};")
        lines.append("}")
    return lines


def _ts_type_for_model_field(fld: django_models.Field) -> str:
    if getattr(fld, "many_to_many", False) or getattr(fld, "one_to_many", False):
        return f"{fld.related_model.__name__}[]"
    if getattr(fld, "many_to_one", False) or getattr(fld, "one_to_one", False):
        return fld.related_model.__name__
    mapping = {
        django_models.AutoField:    "number",
        django_models.IntegerField: "number",
        django_models.FloatField:   "number",
        django_models.DecimalField: "number",
        django_models.BooleanField: "boolean",
        django_models.CharField:    "string",
        django_models.TextField:    "string",
        django_models.DateTimeField:"string",
        django_models.DateField:    "string",
        django_models.JSONField:    "any",
        django_models.DurationField:"string",
        django_models.UUIDField:    "string",
    }
    for cls, ts in mapping.items():
        if isinstance(fld, cls):
            return ts
    return "any"


def export_model_interfaces() -> list[str]:
    lines = ["// AUTO-GENERATED – Model Interfaces"]
    for model in django_apps.get_models():
        lines.append(f"export interface {model.__name__} {{")
        for fld in model._meta.get_fields():
            if fld.auto_created and not getattr(fld, "concrete", False):
                continue
            typ = _ts_type_for_model_field(fld)
            opt = "?" if getattr(fld, "blank", False) or getattr(fld, "null", False) else ""
            lines.append(f"  {fld.name}{opt}: {typ};")
        lines.append("}")
    return lines


def _type_code_for_field(fld: serializers.Field) -> int:
    mapping = {
        serializers.IntegerField: 9,
        serializers.CharField:   18,
        serializers.BooleanField: 3,
        serializers.DateTimeField:16,
        serializers.DecimalField: 15,
    }
    for cls, code in mapping.items():
        if isinstance(fld, cls):
            return code
    return 1


TYPE_CODE_TS_MAP = {
    1:  "any",
    3:  "boolean",
    9:  "number",
    15: "number",
    16: "string",
    18: "string",
}


def _ts_type_for_field(fld: serializers.Field) -> str:
    many = getattr(fld, "many", False)
    if isinstance(fld, PrimaryKeyRelatedField):
        return "number[]" if many else "number"
    if isinstance(fld, SlugRelatedField):
        return "string[]" if many else "string"
    if isinstance(fld, ListSerializer):
        return f"{_ts_type_for_field(fld.child)}[]"
    if isinstance(fld, DRFSerializer) and not isinstance(fld, ModelSerializer):
        return fld.__class__.__name__
    return TYPE_CODE_TS_MAP[_type_code_for_field(fld)]


def export_serializer(serializer: BaseSerializer) -> str:
    name = serializer.__class__.__name__
    lines = [f"export interface {name} {{"]
    for fld_name, fld in serializer.get_fields().items():
        ts = _ts_type_for_field(fld)
        opt = "?" if not getattr(fld, "required", False) else ""
        lines.append(f"  {fld_name}{opt}: {ts};")
    lines.append("}")
    return "\n".join(lines)


def export_serializers() -> list[str]:
    lines = ["// AUTO-GENERATED – Serializer Interfaces"]
    try:
        pkg = import_module(SERIALIZER_PACKAGE)
    except ModuleNotFoundError:
        return lines

    mods = [SERIALIZER_PACKAGE]
    if hasattr(pkg, "__path__"):
        mods += [name for _, name, _ in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + ".")]

    for m in mods:
        module = import_module(m)
        for attr in dir(module):
            cls = getattr(module, attr)
            if (
                inspect.isclass(cls)
                and issubclass(cls, BaseSerializer)
                and cls is not BaseSerializer
                and hasattr(cls, "Meta")
            ):
                try:
                    inst = cls()
                    lines.append(export_serializer(inst))
                except Exception:
                    pass
    return lines


def export_table_dtos() -> list[str]:
    lines = ["// AUTO-GENERATED – Table DTO Configs"]
    mod = import_module("attributes.tables")
    for name, cls in inspect.getmembers(mod, inspect.isclass):
        if issubclass(cls, BaseTableDto) and cls is not BaseTableDto:
            cfg = cls.column_config()
            lines.append(f"export const {name}Columns: Column[] = {json.dumps(cfg, ensure_ascii=False, indent=2)};")
    return lines


def export_form_dtos() -> list[str]:
    import re
    from django.db.models import ForeignKey, ManyToManyField

    lines = [
        "import { FormField } from './core';",
        "import { apiConfigs } from './api_configs';",
        "// AUTO-GENERATED – Form DTO Configs"
    ]
    mod = import_module("attributes.forms")

    for name, cls in inspect.getmembers(mod, inspect.isclass):
        if not issubclass(cls, BaseFormDto) or cls is BaseFormDto:
            continue

        model_cls = getattr(getattr(cls, "Meta", None), "model", None)
        if not model_cls:
            base = name[:-7] if name.endswith("FormDto") else name
            for m in django_apps.get_models():
                if m.__name__ == base:
                    model_cls = m
                    break

        for mode in MODES:
            raw = cls.form_config(mode=mode)
            arr = raw if isinstance(raw, list) else [raw]
            for cfg in arr:
                t = cfg.pop("title", None)
                if t is not None:
                    cfg["label"] = t
                cfg["type"] = str(cfg.get("formAttributes", {}).get("inputType", "text"))
                fld = cfg.get("field")
                if model_cls and fld:
                    try:
                        mf = model_cls._meta.get_field(fld)
                        if isinstance(mf, (ForeignKey, ManyToManyField)):
                            rel = mf.related_model.__name__
                            key = rel[0].lower() + rel[1:] + "API"
                            cfg["api"]        = key
                            cfg["model_name"] = rel
                            cfg["model"]      = rel
                            cfg["serializer"] = rel + "Serializer"
                    except Exception:
                        pass

            const = json.dumps(arr, ensure_ascii=False, indent=2)
            const = re.sub(r'"api":\s*"(\w+API)"', r"api: apiConfigs.\1", const)
            dto = name[:-7] if name.endswith("FormDto") else name
            lines.append(f"export const {dto}_{mode}_Fields: FormField[] = {const};")

    return lines


def export_api_configs() -> list[str]:
    lines = ["// AUTO-GENERATED – API Configs", "export const apiConfigs = {"]
    try:
        urls = import_module("core.api.urls")
        raw = getattr(urls, "urlpatterns", [])
    except ImportError:
        raw = []

    # recursive walker
    def walk(pats):
        for p in pats:
            if isinstance(p, URLPattern):
                yield p
            elif isinstance(p, URLResolver):
                yield from walk(p.url_patterns)

    patterns = list(walk(raw))

    for entry in patterns:
        view = entry.callback
        view_cls = getattr(view, "view_class", None)
        if not view_cls or not issubclass(view_cls, APIView) or view_cls.__name__ == "APIRootView":
            continue

        key    = view_cls.__name__[0].lower() + view_cls.__name__[1:]
        route  = "/" + entry.pattern._route.strip("/")
        method = view_cls.http_method_names[0].upper()

        mn = "any"
        if getattr(view_cls, "queryset", None) is not None:
            mn = view_cls.queryset.model.__name__
        else:
            ser = getattr(view_cls, "serializer_class", None)
            m = getattr(getattr(ser, "Meta", None), "model", None)
            if m:
                mn = m.__name__

        sn = getattr(view_cls, "serializer_class", None)
        sn = sn.__name__ if sn else ""

        lines.append(f"  {key}: {{")
        lines.append(f"    url: '{route}',")
        lines.append(f"    method: '{method}',")
        lines.append(f"    name: '{view_cls.__name__}',")
        lines.append(f"    queryable: {str(method=='GET').lower()},")
        lines.append(f"    model_name: '{mn}',")
        lines.append(f"    model: '{mn}',")
        if sn:
            lines.append(f"    serializer: '{sn}',")
        lines.append("  },")

    lines.append("};")
    return lines


def export_all_ts(output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "core.ts").write_text(
        "\n".join(export_core_interfaces()), encoding="utf-8"
    )
    (output_dir / "models.ts").write_text(
        "\n".join(export_model_interfaces()), encoding="utf-8"
    )
    (output_dir / "serializers.ts").write_text(
        "\n".join(export_serializers()), encoding="utf-8"
    )
    (output_dir / "tables.ts").write_text(
        "import { Column } from './core';\n\n" + "\n".join(export_table_dtos()), encoding="utf-8"
    )
    (output_dir / "forms.ts").write_text(
        "\n".join(export_form_dtos()), encoding="utf-8"
    )
    (output_dir / "api_configs.ts").write_text(
        "\n".join(export_api_configs()), encoding="utf-8"
    )

    print(f"✅ Generated TS files in {output_dir}")

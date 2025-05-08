import inspect
import json
import pkgutil
import re
from importlib import import_module
from pathlib import Path

from django.apps import apps as django_apps
from django.db import models as django_models
from django.urls import URLPattern
from rest_framework import serializers
from rest_framework.generics import (
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)
from rest_framework.relations import (
    PrimaryKeyRelatedField,
    SlugRelatedField
)
from rest_framework.serializers import (
    BaseSerializer,
    ListSerializer,
    Serializer as DRFSerializer, ModelSerializer
)
from rest_framework.views import APIView

from attributes.forms import BaseFormDto

MODES = ("create", "update", "view")
SERIALIZER_PACKAGE = "core.api.serializers"
OUTPUT_DIR = Path("templates/ts_converter")


CORE_INTERFACES = {
    "Column": {
        "alanIsmi": "string",
        "anahtar": "string",
        "hidden?": "boolean",
        "typeCode?": "number",
        "kolonAttributelar?": "{ [key: string]: any }",
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
    },
}

def export_core_interfaces() -> list[str]:
    lines = ["// AUTO-GENERATED – Core Interfaces"]
    for name, props in CORE_INTERFACES.items():
        lines.append(f"export interface {name} {{")
        for key, ts_type in props.items():
            lines.append(f"  {key}: {ts_type};")
        lines.append("}")
    return lines


def _ts_type_for_model_field(field: django_models.Field) -> str:
    if getattr(field, "many_to_many", False) or getattr(field, "one_to_many", False):
        return f"{field.related_model.__name__}[]"
    if getattr(field, "many_to_one", False) or getattr(field, "one_to_one", False):
        return field.related_model.__name__
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
        if isinstance(field, cls):
            return ts
    return "any"

def export_model_interfaces() -> list[str]:
    lines = ["// AUTO-GENERATED – Model Interfaces"]
    for model in django_apps.get_models():
        lines.append(f"export interface {model.__name__} {{")
        for fld in model._meta.get_fields():
            if fld.auto_created and not getattr(fld, "concrete", False):
                continue
            ts = _ts_type_for_model_field(fld)
            opt = "?" if getattr(fld, "blank", False) or getattr(fld, "null", False) else ""
            lines.append(f"  {fld.name}{opt}: {ts};")
        lines.append("}")
    return lines


def _type_code_for_field(fld: serializers.Field) -> int:
    mapping = {
        serializers.IntegerField:   9,
        serializers.CharField:     18,
        serializers.BooleanField:   3,
        serializers.DateTimeField: 16,
        serializers.DecimalField:  15,
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
    lines = []
    try:
        pkg = import_module(SERIALIZER_PACKAGE)
    except ModuleNotFoundError:
        return lines

    modules = [SERIALIZER_PACKAGE]
    if hasattr(pkg, "__path__"):
        modules += [n for _, n, _ in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + ".")]

    for mod_str in modules:
        mod = import_module(mod_str)
        for attr in dir(mod):
            cls = getattr(mod, attr)
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
    import json, inspect
    from importlib import import_module
    from attributes.tables import BaseTableDto

    TYPECODE_MAP = {
        9:  "coreLib_Int32",
        18: "coreLib_String",
        3:  "coreLib_Boolean",
        16: "coreLib_DateTime",
        15: "coreLib_Decimal",
    }

    def to_pascal(s: str) -> str:
        return "".join(w.capitalize() for w in s.split("_"))

    def to_camel(s: str) -> str:
        p = to_pascal(s)
        return p[0].lower() + p[1:] if p else ""

    lines = []
    mod = import_module("attributes.tables")

    for name, cls in inspect.getmembers(mod, inspect.isclass):
        if not (issubclass(cls, BaseTableDto) and cls is not BaseTableDto):
            continue

        type_id   = getattr(cls, "tipId", name)
        type_name = getattr(cls, "tipIsmi", name)
        attributes  = getattr(getattr(cls, "Meta", None), "nitelikTipIsmi", None)

        tablo_attrs = []
        if hasattr(cls, "table_config"):
            try:
                tablo_attrs = cls.table_config() or []
            except:
                pass

        kolonlar = []
        for raw in cls.column_config():
            fld      = raw.get("field")
            pascal   = to_pascal(fld)
            camel    = to_camel(fld)
            tip_kodu = raw.get("typeCode")

            column_attributes = list(raw.get("kolonAttributelar", []))

            kolonlar.append({
                "alanIsmi":         pascal,
                "anahtar":          camel,
                "tipKodu":          tip_kodu,
                "kolonAttributelar": column_attributes,
                "objeTipId":        TYPECODE_MAP.get(tip_kodu, "any"),
                "bosOlabilir":      False,
                "enumTipi":         False,
            })

        payload = {
            "tipIsmi":           type_name,
            "tipId":             type_id,
            "nitelikTipIsmi":    attributes,
            "kolonTanimlar":     kolonlar,
            "tabloAttributelar": tablo_attrs,
        }

        blob = json.dumps(payload, ensure_ascii=False, indent=2)
        lines.append(f"export const {type_id} = {blob};")

    return lines


def export_form_dtos() -> list[str]:
    from django.db.models import ForeignKey, ManyToManyField

    lines = [
        "import { FormField } from './core';",
        "import { apiConfigs } from './api_configs';",
    ]
    mod = import_module("attributes.forms")
    for name, cls in inspect.getmembers(mod, inspect.isclass):
        if not (issubclass(cls, BaseFormDto) and cls is not BaseFormDto):
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
                title = cfg.pop("title", None)
                if title:
                    cfg["label"] = title
                cfg["type"] = str(cfg.get("formAttributes", {}).get("inputType", "text"))
                fld = cfg.get("field")
                if model_cls and fld:
                    try:
                        mf = model_cls._meta.get_field(fld)
                        if isinstance(mf, (ForeignKey, ManyToManyField)):
                            rel = mf.related_model.__name__
                            key = rel[0].lower() + rel[1:] + "API"
                            cfg["api"] = key
                    except Exception:
                        pass

            const = json.dumps(arr, ensure_ascii=False, indent=2)
            const = re.sub(r'"api":\s*"(\w+API)"', r'api: apiConfigs.\1', const)
            dto = name[:-7] if name.endswith("FormDto") else name
            lines.append(f"export const {dto}_{mode}_Fields: FormField[] = {const};")

    return lines


def export_typeInformation() -> list[str]:
    from rest_framework.serializers import BaseSerializer
    lines = [
        "export const typeInformation = {",
    ]
    for model in django_apps.get_models():
        nm = model.__name__
        lines.append(f"  {nm}: {{ tipIsmi: \"{nm}\" }},")
    try:
        pkg = import_module(SERIALIZER_PACKAGE)
        modules = [SERIALIZER_PACKAGE]
        if hasattr(pkg, "__path__"):
            modules += [n for _, n, _ in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + ".")]
        for mod_str in modules:
            mod = import_module(mod_str)
            for attr in dir(mod):
                cls = getattr(mod, attr)
                if (
                    inspect.isclass(cls)
                    and issubclass(cls, BaseSerializer)
                    and cls is not BaseSerializer
                    and hasattr(cls, "Meta")
                ):
                    nm = cls.__name__
                    lines.append(f"  {nm}: {{ tipIsmi: \"{nm}\" }},")
    except ImportError:
        pass

    lines.append("};")
    return lines


def export_api_configs() -> list[str]:
    lines = []
    used_models = set()
    used_serializers = set()
    entries = []

    try:
        urls = import_module("core.api.urls")
        patterns = getattr(urls, "urlpatterns", [])
    except ImportError:
        patterns = []

    for entry in patterns:
        if not isinstance(entry, URLPattern):
            continue
        view_cls = getattr(entry.callback, "view_class", None)
        if not (view_cls and issubclass(view_cls, APIView)) or view_cls.__name__ == "APIRootView":
            continue

        key   = view_cls.__name__[0].lower() + view_cls.__name__[1:]
        route = "/" + entry.pattern._route.strip("/")
        if issubclass(view_cls, DestroyAPIView):
            method, queryable = "DELETE", False
        elif issubclass(view_cls, UpdateAPIView):
            method, queryable = "PUT", False
        elif issubclass(view_cls, CreateAPIView):
            method, queryable = "POST", False
        else:
            method, queryable = "GET", True

        mn = "any"
        if getattr(view_cls, "queryset", None) is not None:
            mn = view_cls.queryset.model.__name__
        else:
            ser = getattr(view_cls, "serializer_class", None)
            meta = getattr(ser, "Meta", None)
            if meta and getattr(meta, "model", None):
                mn = meta.model.__name__

        sn = getattr(view_cls, "serializer_class", None)
        sn = sn.__name__ if sn else ""

        used_models.add(mn)
        if sn:
            used_serializers.add(sn)

        entries.append((key, route, method, queryable, view_cls.__name__, mn, sn))

    lines.append("import { typeInformation } from './models';")

    lines.append("export const apiConfigs = {")
    for key, route, method, queryable, cname, mn, sn in entries:
        lines.extend([
            f"  {key}: {{",
            f"    link         : '{route}',",
            f"    metot        : '{method}',",
            f"    sorguIsim    : '{cname}',",
            f"    queryable    : {str(queryable).lower()},",
            f"    dtoTipId     : '{mn}',",
            f"    dtoTipBilgi  : typeInformation.{mn},",
            f"    sorguTipId   : '{sn}',",
            f"    sorguTipBilgi: typeInformation.{sn},",
            f"  }},",
        ])
    lines.append("};")
    return lines


def export_all_ts(output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "core.ts").write_text("\n".join(export_core_interfaces()), encoding="utf-8")

    combined = (
        export_model_interfaces()
        + [""]
        + export_serializers()
        + [""]
        + export_typeInformation()
    )
    (output_dir / "models.ts").write_text("\n".join(combined), encoding="utf-8")

    (output_dir / 'tables.ts').write_text(
        "import { Column } from './core';\n\n"
        + "\n".join(export_table_dtos()),
        encoding='utf-8'
    )

    (output_dir / "forms.ts").write_text("\n".join(export_form_dtos()), encoding="utf-8")

    (output_dir / "api_configs.ts").write_text("\n".join(export_api_configs()), encoding="utf-8")

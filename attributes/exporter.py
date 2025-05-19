import inspect
import pkgutil
from importlib import import_module
from pathlib import Path

from django.apps import apps as django_apps
from django.db import models as django_models
from rest_framework import serializers
from rest_framework.serializers import (
    BaseSerializer,
    Serializer as DRFSerializer,
    ModelSerializer,
)

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
}

TYPECODE_MAP = {
    9: "coreLib_Int32",
    18: "coreLib_String",
    3: "coreLib_Boolean",
    16: "coreLib_DateTime",
    15: "coreLib_Decimal",
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
        django_models.AutoField: "number",
        django_models.IntegerField: "number",
        django_models.FloatField: "number",
        django_models.DecimalField: "number",
        django_models.BooleanField: "boolean",
        django_models.CharField: "string",
        django_models.TextField: "string",
        django_models.DateTimeField: "string",
        django_models.DateField: "string",
        django_models.JSONField: "any",
        django_models.DurationField: "string",
        django_models.UUIDField: "string",
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
        serializers.IntegerField: 9,
        serializers.CharField: 18,
        serializers.BooleanField: 3,
        serializers.DateTimeField: 16,
        serializers.DecimalField: 15,
    }
    for cls, code in mapping.items():
        if isinstance(fld, cls):
            return code
    return 1


def _ts_type_for_field(fld: serializers.Field) -> str:
    SERIALIZER_TYPE_MAP = {
        1: "any",
        3: "coreLib_Boolean",
        9: "coreLib_Int32",
        15: "coreLib_Decimal",
        16: "coreLib_DateTime",
        18: "coreLib_String",
    }
    code = _type_code_for_field(fld)
    if isinstance(fld, DRFSerializer) and not isinstance(fld, ModelSerializer):
        return fld.__class__.__name__
    return f'"{SERIALIZER_TYPE_MAP.get(code, "any")}"'


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
    import inspect, json
    from importlib import import_module
    from django.db.models import ForeignKey, ManyToManyField
    from django.urls import URLPattern
    from rest_framework.views import APIView
    from attributes.tables import BaseTableDto

    # 1) api_configs içinden model→configKey haritası
    api_map: dict[str, str] = {}
    try:
        urls_mod = import_module("core.api.urls")
        for entry in getattr(urls_mod, "urlpatterns", []):
            if not isinstance(entry, URLPattern):
                continue
            view_cls = getattr(entry.callback, "view_class", None)
            if not (view_cls and issubclass(view_cls, APIView)):
                continue
            key = view_cls.__name__[0].lower() + view_cls.__name__[1:]
            model_cls = None
            if hasattr(view_cls, "queryset") and view_cls.queryset is not None:
                model_cls = view_cls.queryset.model
            else:
                ser = getattr(view_cls, "serializer_class", None)
                meta = getattr(ser, "Meta", None)
                model_cls = getattr(meta, "model", None)
            if model_cls:
                api_map[model_cls._meta.object_name] = key
    except ImportError:
        pass

    TYPECODE_MAP = {
        9: "coreLib_Int32",
        18: "coreLib_String",
        3: "coreLib_Boolean",
        16: "coreLib_DateTime",
        15: "coreLib_Decimal",
    }

    lines: list[str] = [
        "import { Column } from './core';",
        "import { apiConfigs } from './api_configs';",
        "",
    ]
    lines.extend(export_typeInformation())
    lines.append("")

    tables_mod = import_module("attributes.tables")
    for name, tbl_cls in inspect.getmembers(tables_mod, inspect.isclass):
        if not issubclass(tbl_cls, BaseTableDto) or tbl_cls is BaseTableDto:
            continue

        tip_id = getattr(tbl_cls, "tipId", name)
        tip_name = getattr(tbl_cls, "tipIsmi", name)
        meta_nitl = getattr(getattr(tbl_cls, "Meta", None), "nitelikTipIsmi", None)
        model_cls = getattr(getattr(tbl_cls, "Meta", None), "model", None)

        lines.append(f"export const {tip_id} = {{")
        lines.append(f'  tipIsmi: "{tip_name}",')
        lines.append(f'  tipId: "{tip_id}",')
        lines.append(f'  nitelikTipIsmi: {json.dumps(meta_nitl)},')
        lines.append("  kolonTanimlar: [")

        for raw in tbl_cls.column_config():
            fld = raw["field"]
            pascal = "".join(w.capitalize() for w in fld.split("_"))
            camel = pascal[0].lower() + pascal[1:]
            tip_kodu = raw.get("typeCode")
            attrs = raw.get("kolonAttributelar", [])

            lines.append("    {")
            lines.append(f'      alanIsmi: "{pascal}",')
            lines.append(f'      anahtar: "{camel}",')
            lines.append(f'      tipKodu: {tip_kodu if tip_kodu is not None else "null"},')
            lines.append("      kolonAttributelar: [")

            if model_cls:
                try:
                    dj_fld = model_cls._meta.get_field(fld)
                except:
                    dj_fld = None
                if isinstance(dj_fld, (ForeignKey, ManyToManyField)):
                    related = dj_fld.remote_field.model._meta.object_name
                    cfg_key = api_map.get(related, related[0].lower() + related[1:])
                    lines.append("        {")
                    lines.append(f'          tipIsmi: "alanSecimSecenekTipi{pascal}",')
                    lines.append("          obje: {")
                    lines.append(
                        f'            sorguObje: {{ '
                        f'ustSecenekId: null, '
                        f'tabloAdi: "{related}", '
                        f'kolonAdi: "{fld}", '
                        f'secenekTipi: null '
                        f'}},'
                    )
                    lines.append(
                        f'            sorguTipId: `{cfg_key}`,'
                    )
                    lines.append("            etiketAnahtarlar: null,")
                    lines.append("            aciklamaAnahtar: null,")
                    lines.append("            excelAnahtar: null,")
                    lines.append("            yalnizFiltrelerdeSecim: false")
                    lines.append("          }")
                    lines.append("        },")

            # diğer attribute’lar
            for attr in attrs:
                blob = json.dumps(attr, ensure_ascii=False)
                lines.append(f"        {blob},")

            lines.append("      ],")
            lines.append(f'      objeTipId: "{TYPECODE_MAP.get(tip_kodu, "any")}",')
            lines.append("      bosOlabilir: false,")
            lines.append("      enumTipi: false")
            lines.append("    },")

        lines.append("  ],")
        lines.append("  tabloAttributelar: []")
        lines.append("};")
        lines.append("")

    return lines


def export_typeInformation() -> list[str]:
    import inspect
    import pkgutil
    from importlib import import_module
    from rest_framework.serializers import BaseSerializer
    from attributes.tables import BaseTableDto

    lines: list[str] = ["export const typeInformation = {"]
    seen: set[str] = set()

    # 1) Table DTO’ları
    tables_mod = import_module("attributes.tables")
    for name, cls in inspect.getmembers(tables_mod, inspect.isclass):
        if issubclass(cls, BaseTableDto) and cls is not BaseTableDto:
            if name in seen:
                continue
            tip = getattr(cls, "tipTanim", name)
            lines.append(f'  {name}: {{ tipTanim: "{tip}" }},')
            seen.add(name)

    # 2) Serializer’lar
    try:
        ser_pkg = import_module(SERIALIZER_PACKAGE)
        modules = [SERIALIZER_PACKAGE]
        if hasattr(ser_pkg, "__path__"):
            modules += [
                n for _, n, _ in pkgutil.walk_packages(ser_pkg.__path__, ser_pkg.__name__ + ".")
            ]
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
                    name = cls.__name__
                    if name in seen:
                        continue
                    lines.append(f'  {name}: {{ tipTanim: "{name}" }},')
                    seen.add(name)
    except ImportError:
        pass

    lines.append("};")
    return lines


def _gather_patterns(urlpatterns):
    from django.urls import URLPattern, URLResolver
    for entry in urlpatterns:
        if isinstance(entry, URLPattern):
            yield entry
        elif isinstance(entry, URLResolver):
            # rekürsif olarak içine gir
            yield from _gather_patterns(entry.url_patterns)


def export_api_configs() -> list[str]:
    """
    Sadece READ (GET) endpoint’lerini üretir.
    CREATE / UPDATE / DELETE endpoint’leri komut dosyasına taşındı.
    """
    from django.urls import URLPattern
    from rest_framework.views import APIView
    from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
    from core.api.urls import urlpatterns, router

    lines: list[str] = [
        "import { typeInformation } from './tables';",
        "",
        "export const apiConfigs = {",
    ]

    def make_entry(key: str, route: str, view_cls, method: str, queryable: bool) -> list[str]:
        # dtoTipId / dtoTipBilgi: table_dto varsa onu, yoksa serializer’dan türet
        table_name = getattr(view_cls, "table_dto", None)
        if not table_name:
            ser = getattr(view_cls, "serializer_class", None)
            if ser and ser.__name__.endswith("Serializer"):
                table_name = ser.__name__[:-10] + "Table"
            else:
                table_name = "anyTable"
        # sorguTipId / sorguTipBilgi
        ser = getattr(view_cls, "serializer_class", None)
        sn = ser.__name__ if ser else ""

        return [
            f"  {key}: {{",
            f"    link         : '{route}',",
            f"    metot        : '{method}',",
            f"    sorguIsim    : '{view_cls.__name__}',",
            f"    queryable    : {str(queryable).lower()},",
            f"    dtoTipId     : '{table_name}',",
            f"    dtoTipBilgi  : typeInformation.{table_name},",
            f"    sorguTipId   : '{sn}',",
            f"    sorguTipBilgi: typeInformation.{sn},",
            f"  }},",
        ]

    # 1) path() ile tanımlanan APIView’ler (sadece GET)
    for entry in urlpatterns:
        if not isinstance(entry, URLPattern):
            continue
        view_cls = getattr(entry.callback, "view_class", None)
        if (
                not view_cls
                or not issubclass(view_cls, APIView)
                or view_cls.__name__ == "APIRootView"
                or issubclass(view_cls, (CreateAPIView, UpdateAPIView, DestroyAPIView))
        ):
            continue

        key = view_cls.__name__[0].lower() + view_cls.__name__[1:]
        route = "/" + entry.pattern._route.strip("/")

        # GET endpoint
        lines += make_entry(key, route, view_cls, "GET", True)

    # 2) router.register ile eklenen ViewSet’ler (GET list & detail)
    for prefix, viewset_cls, _ in router.registry:
        if viewset_cls.__name__ == "APIRootView":
            continue

        key = prefix.replace("-", "")
        route = f"/{prefix}/"
        # ViewSet’ten list endpoint (GET) olarak kaydediyoruz
        lines += make_entry(key, route, viewset_cls, "GET", True)

    lines.append("};")
    return lines


def export_command_configs() -> list[str]:
    """
    Create/Update/Delete endpoint’leri için komut akış yapılandırması üretir.
    Her view_class içinde tanımlı `table_dto` özniteliğini öncelikli olarak kullanır.
    """
    from django.urls import URLPattern
    from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
    from core.api.urls import urlpatterns

    lines: list[str] = [
        "import { typeInformation } from './tables';",
        "",
        "export const commandsInformation = {",
    ]

    for entry in urlpatterns:
        if not isinstance(entry, URLPattern):
            continue
        view_cls = getattr(entry.callback, "view_class", None)
        if not view_cls:
            continue

        # Sadece Create/Update/Delete sınıfları
        if issubclass(view_cls, CreateAPIView):
            komut_aciş = "Create"
        elif issubclass(view_cls, UpdateAPIView):
            komut_aciş = "Update"
        elif issubclass(view_cls, DestroyAPIView):
            komut_aciş = "Delete"
        else:
            continue

        # TS anahtarı: sınıf adı + komut türü
        key = view_cls.__name__[0].lower() + view_cls.__name__[1:] + komut_aciş

        route = "/" + entry.pattern._route.strip("/")

        # dtoTipId / istekTipBilgi: table_dto özniteliği varsa onu, yoksa serializer’dan türet
        table_name = getattr(view_cls, "table_dto", None)
        if not table_name:
            ser = getattr(view_cls, "serializer_class", None)
            sn = ser.__name__ if ser else ""
            table_name = sn[:-len("Serializer")] + "Table" if sn.endswith("Serializer") else "anyTable"

        # Komut akış tipi ID’si
        komut_akis = f"{view_cls.__name__}CommandFlow"

        lines.extend([
            f"  {key}: {{",
            f"    link          : '{route}',",
            f"    istekTipId    : '{table_name}',",
            f"    istekTipBilgi : typeInformation.{table_name},",
            f"    komutAkisTipId: '{komut_akis}',",
            f"  }},",
        ])

    lines.append("};")
    return lines


def export_all_ts(output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)

    # core.ts
    (output_dir / "core.ts").write_text(
        "\n".join(export_core_interfaces()), encoding="utf-8"
    )

    models_lines = (
            export_model_interfaces()
            + [""]
            + export_serializers()
    )
    (output_dir / "models.ts").write_text(
        "\n".join(models_lines), encoding="utf-8"
    )

    # tables.ts
    table_lines = export_table_dtos()
    (output_dir / "tables.ts").write_text(
        "\n".join(table_lines),
        encoding="utf-8"
    )

    # api_configs.ts
    (output_dir / "api_configs.ts").write_text(
        "\n".join(export_api_configs()), encoding="utf-8"
    )

    commands = export_command_configs()
    (output_dir / "commands.ts").write_text(
        "\n".join(commands),
        encoding="utf-8"
    )

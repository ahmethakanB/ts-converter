# attributes/exporter.py
from importlib import import_module
import inspect
import json
from pathlib import Path

from rest_framework import serializers
from attributes.tables import BaseTableDto
from attributes.forms import BaseFormDto
from core.api.serializers import OrderDetailSerializer  # Tablo için

TS_TARGET = "templates/ts_converter/columns.ts"
MODES = ("create", "update", "view")


def _type_code_for_field(field: serializers.Field) -> int:
    if isinstance(field, serializers.IntegerField):    return 9
    if isinstance(field, serializers.CharField):       return 18
    if isinstance(field, serializers.BooleanField):    return 3
    if isinstance(field, serializers.DateTimeField):   return 16
    if isinstance(field, serializers.DecimalField):    return 15
    return 1


def generate_merged_columns(dto_class, serializer_class) -> list[dict]:
    """WorkDetailTable gibi, serializer’la merge edilmesi gereken tablolar için."""
    instance = serializer_class()
    dto_fields = {col["field"]: col for col in dto_class.column_config()}
    columns = []

    for name, field in instance.get_fields().items():
        dto_col = dto_fields.get(name, {})

        col = {
            "field": name,
            "title": dto_col.get("title", name.replace("_", " ").title()),
            "typeCode": dto_col.get("typeCode", _type_code_for_field(field)),
            "tableAttributes": dict(dto_col.get("tableAttributes", {})),
        }
        # root özelliklerini de ekle (hidden, vs.)
        for k, v in dto_col.items():
            if k not in col and k not in ("field", "title", "typeCode", "tableAttributes"):
                col[k] = v

        columns.append(col)

    return columns


def export_all_ts(outfile: Path | str = TS_TARGET):
    outfile = Path(outfile)
    TEMPLATE = """\
// AUTO-GENERATED – do not edit by hand

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
  title: string;
  type: string;
  required?: boolean;
  disabled?: boolean;
  formAttributes?: { [key: string]: any };
  [key: string]: any;
}

"""
    sections = [TEMPLATE]

    # ── 1) Table DTO’ları ─────────────────────────────────────────
    dto_mod = import_module("attributes.tables")
    for name, cls in inspect.getmembers(dto_mod, inspect.isclass):
        if not issubclass(cls, BaseTableDto) or cls is BaseTableDto:
            continue

        # Eğer WorkDetailTable gibi özel merge istersen
        if name == "WorkDetailTable":
            data = generate_merged_columns(cls, OrderDetailSerializer)
        else:
            data = cls.column_config()

        sections.append(
            f"export const {name}Columns: Column[] = "
            + json.dumps(data, ensure_ascii=False, indent=2)
            + " as const;\n"
        )

    # ── 2) Form DTO’ları (mode bazlı) ─────────────────────────────
    form_mod = import_module("attributes.forms")
    for name, cls in inspect.getmembers(form_mod, inspect.isclass):
        if not issubclass(cls, BaseFormDto) or cls is BaseFormDto:
            continue

        for mode in MODES:
            data = cls.form_config(mode=mode)
            const_name = f"{name}_{mode}_Fields"
            sections.append(
                f"export const {const_name} = "
                + json.dumps(data, ensure_ascii=False, indent=2)
                + " as const;\n"
            )

    outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_text("\n".join(sections), encoding="utf8")
    return outfile

from typing import List, Dict

from attributes.dsl import column
from attributes.flags.table_root import type_code
from attributes.flags.table import column_hide, column_search, column_order
from attributes.flags.typecodes import TypeCode


class BaseTableDto:
    @classmethod
    def column_config(cls) -> List[Dict]:
        cols: List[Dict] = []

        for name, member in cls.__dict__.items():
            fn = member.__func__ if isinstance(member, staticmethod) else member
            if not callable(fn):
                continue

            try:
                data = fn()
            except TypeError:
                continue

            if isinstance(data, dict):
                # 🔥 Eksikse field olarak metot adını ekle
                data.setdefault("field", name)
                cols.append(data)

        return cols

class WorkDetailTable(BaseTableDto):

    @staticmethod
    @column_hide
    @type_code(TypeCode.Int32)
    def id():
        return column("ID")

    @staticmethod
    @type_code(TypeCode.String)
    @column_order
    def name():
        return column("İş Detayı Adı")

    @staticmethod
    def products():
        return column("Ürünler")

    @staticmethod
    def type():
        return column("Sipariş Tipi")

    @staticmethod
    @type_code(TypeCode.DateTime)
    def start_datetime():
        return column("Başlangıç Zamanı")

    @staticmethod
    @type_code(TypeCode.DateTime)
    def end_datetime():
        return column("Bitiş Zamanı")

    @staticmethod
    @type_code(TypeCode.String)
    @column_search
    def order_type():
        return column("Sipariş Tipi")
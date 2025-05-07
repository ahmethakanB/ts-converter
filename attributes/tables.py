from typing import List, Dict

from attributes.dsl import column
from attributes.flags.custom_table_attribute import kolonIsmiAttribute, birincilAnahtarAttribute
from attributes.flags.table_root import tipKodu
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
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute
    @birincilAnahtarAttribute
    def id():
        return column("ID")

    @staticmethod
    @tipKodu(TypeCode.String)
    @column_order
    @kolonIsmiAttribute
    def name():
        return column("İş Detayı Adı")

    @staticmethod
    def products():
        return column("Ürünler")

    @staticmethod
    def type():
        return column("Sipariş Tipi")

    @staticmethod
    @tipKodu(TypeCode.DateTime)
    def start_datetime():
        return column("Başlangıç Zamanı")

    @staticmethod
    @tipKodu(TypeCode.DateTime)
    def end_datetime():
        return column("Bitiş Zamanı")

    @staticmethod
    @tipKodu(TypeCode.String)
    @column_search
    def order_type():
        return column("Sipariş Tipi")
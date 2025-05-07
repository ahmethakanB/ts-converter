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
    @kolonIsmiAttribute("ID")
    @birincilAnahtarAttribute
    def id():
        return column()

    @staticmethod
    @tipKodu(TypeCode.String)
    @column_order
    @kolonIsmiAttribute("İş Detayı Adı")
    def name():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Ürünler")
    def products():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Sipariş Tipi")
    def type():
        return column()

    @staticmethod
    @tipKodu(TypeCode.DateTime)
    @kolonIsmiAttribute("Başlangıç Zamanı")
    def start_datetime():
        return column()

    @staticmethod
    @tipKodu(TypeCode.DateTime)
    @kolonIsmiAttribute("Bitiş Zamanı")
    def end_datetime():
        return column()

    @staticmethod
    @tipKodu(TypeCode.String)
    @column_search
    @kolonIsmiAttribute("Sipariş Tipi")
    def order_type():
        return column()

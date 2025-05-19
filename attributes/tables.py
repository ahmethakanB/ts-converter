from typing import List, Dict

from attributes.dsl import column
from attributes.flags.custom_table_attribute import kolonIsmiAttribute, birincilAnahtarAttribute
from attributes.flags.table_root import tipKodu
from attributes.flags.typecodes import TypeCode
from core.models import Order, Product, OrderType


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
    class Meta:
        model = Order

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("ID")
    @birincilAnahtarAttribute
    def id():
        return column()

    @staticmethod
    @kolonIsmiAttribute("İş Detayı Adı")
    @tipKodu(TypeCode.String)
    def name():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("Ürünler")
    def products():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("Sipariş Tipi")
    def type():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Başlangıç Zamanı")
    @tipKodu(TypeCode.DateTime)
    def start_datetime():
        return column()

    @staticmethod
    @tipKodu(TypeCode.DateTime)
    @kolonIsmiAttribute("Bitiş Zamanı")
    def end_datetime():
        return column()


class OrderTable(BaseTableDto):
    class Meta:
        model = Order

    @staticmethod
    @birincilAnahtarAttribute
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("ID")
    def id():
        return column()

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Sipariş Adı")
    def name():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Açıklama")
    def description():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Başlangıç Zamanı")
    @tipKodu(TypeCode.DateTime)
    def start_datetime():
        return column()

    @staticmethod
    @tipKodu(TypeCode.DateTime)
    @kolonIsmiAttribute("Bitiş Zamanı")
    def end_datetime():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Sipariş Tipi")
    @tipKodu(TypeCode.String)
    def type():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @birincilAnahtarAttribute
    @kolonIsmiAttribute("Ürünler")
    def products():
        return column()


class OrderTypeTable(BaseTableDto):
    class Meta:
        model = OrderType

    @staticmethod
    @birincilAnahtarAttribute
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("ID")
    def id():
        return column()

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Sipariş Adı")
    def name():
        return column()


class ProductTable(BaseTableDto):
    class Meta:
        model = Product

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("ID")
    @birincilAnahtarAttribute
    def id():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Ürün Adı")
    @tipKodu(TypeCode.String)
    def name():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("Fiyat")
    def price():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("Stok")
    def stock():
        return column()


class CreateOrder(BaseTableDto):
    class Meta:
        model = Order

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Sipariş Adı")
    def name():
        return column()

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Açıklama")
    def description():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Sipariş Tipi")
    @tipKodu(TypeCode.String)
    def type():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("Ürünler")
    def products():
        return column()


class DeleteOrder(BaseTableDto):
    class Meta:
        model = Order

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Sipariş Adı")
    def id():
        return column()


class UpdateOrder(BaseTableDto):
    class Meta:
        model = Order

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Sipariş Adı")
    def name():
        return column()

    @staticmethod
    @tipKodu(TypeCode.String)
    @kolonIsmiAttribute("Açıklama")
    def description():
        return column()

    @staticmethod
    @kolonIsmiAttribute("Sipariş Tipi")
    @tipKodu(TypeCode.String)
    def type():
        return column()

    @staticmethod
    @tipKodu(TypeCode.Int32)
    @kolonIsmiAttribute("Ürünler")
    def products():
        return column()

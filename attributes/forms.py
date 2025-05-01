# attributes/forms.py
import inspect
from typing import List, Dict

from attributes.dsl import field
from attributes.flags.forms_root import (
    show_in,
    required_in,
    disabled_in,
    text, textarea, datetime_, select, multiselect, hidden
)

class BaseFormDto:
    @classmethod
    def form_config(cls, mode: str = "create") -> List[Dict]:
        fields: List[Dict] = []

        for name, member in cls.__dict__.items():
            fn = member.__func__ if isinstance(member, staticmethod) else member
            if not callable(fn):
                continue

            sig = inspect.signature(fn)
            data = fn(mode=mode) if "mode" in sig.parameters else fn()
            if not isinstance(data, dict):
                continue

            data.setdefault("field", name)
            fields.append(data)

        # **view** moddaysa tüm alanları disable et
        if mode == "view":
            for f in fields:
                fa = f.setdefault("formAttributes", {})
                fa["disabled"] = True

        return fields


class OrderFormDto(BaseFormDto):

    # id yalnızca update ve view’de görünsün, update’de disabled de
    @staticmethod
    @show_in("update", "view")
    @hidden
    @disabled_in("update", "view")
    def id(mode: str = None):
        return field("ID")

    # name yalnızca create modunda required olsun
    @staticmethod
    @required_in("create")
    @text
    def name(mode: str = None):
        return field("Sipariş Adı")

    @staticmethod
    @textarea
    def description(mode: str = None):
        return field("Açıklama")

    @staticmethod
    @required_in("create")
    @datetime_
    def start_datetime(mode: str = None):
        return field("Başlangıç Zamanı")

    @staticmethod
    @datetime_
    def end_datetime(mode: str = None):
        return field("Bitiş Zamanı")

    @staticmethod
    @required_in("create")
    @select
    def type(mode: str = None):
        return field("Sipariş Tipi")

    @staticmethod
    @multiselect
    def products(mode: str = None):
        return field("Ürünler")

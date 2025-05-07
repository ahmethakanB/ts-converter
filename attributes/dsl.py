from typing import Dict

def _ensure_attrs(col: Dict) -> Dict:
    col.setdefault("tableAttributes", {})
    return col["tableAttributes"]

def column(title: str, **extra) -> Dict:
    """
    title: Kolon başlığı.
    extra: İsterseniz statik ek alanlar.
    """
    base: Dict = {
        # API’deki karşılığı "alanIsmi", frontend’te bizi ilgilendiren başlık:
        # "title": title,
        # artık tablo attribute’leri bu listede saklanacak:
        "kolonAttributelar": [],
    }
    base.update(extra)
    return base

def field(title: str, **extra) -> Dict:
    """
    title: Ekranda gösterilecek başlık.
    extra: Ekstra formAttributes (placeholder, vs.).
    """
    return {
        "title": title,
        "formAttributes": {},  # inputType, required, disabled vs. dekoratörlerle eklenir
        **extra
    }

# TODO modeller için oluştur

from typing import Dict


def _ensure_attrs(col: Dict) -> Dict:
    col.setdefault("tableAttributes", {})
    return col["tableAttributes"]


def column(*args, **extra) -> Dict:
    """
    @column() veya @column("ignoredTitle", foo=bar) –
    positional arg (başlık) görmezden gelinir,
    extra dict içindeki anahtarlar köke eklenir.
    """
    base: Dict = {
        "kolonAttributelar": [],  # attribute listesi
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

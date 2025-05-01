from typing import Dict

def _ensure_attrs(col: Dict) -> Dict:
    col.setdefault("tableAttributes", {})
    return col["tableAttributes"]

def column(title: str, **extra) -> Dict:
    """extra anahtarları doğrudan KÖK’e ekler (istenirse)."""
    base = {
        "title": title,
        "tableAttributes": {}
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
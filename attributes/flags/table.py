from functools import wraps
from typing import Dict, Callable

def _ensure_attrs(col: Dict) -> list:
    # kolonAttributelar zaten column() içinde tanımlı
    return col.setdefault("kolonAttributelar", [])

def column_hide(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_hide → listeye kolonHideAttribute ekler"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data).append({
            "tipIsmi": "kolonHideAttribute",
            "obje": {}
        })
        return data
    return wrapper

def column_order(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_order → listeye kolonOrderableAttribute ekler"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data).append({
            "tipIsmi": "kolonOrderableAttribute",
            "obje": {}
        })
        return data
    return wrapper

def column_search(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_search → listeye kolonSearchableAttribute ekler"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data).append({
            "tipIsmi": "kolonSearchableAttribute",
            "obje": {}
        })
        return data
    return wrapper

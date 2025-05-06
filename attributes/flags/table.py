from functools import wraps
from typing import Dict, Callable


def _ensure_attrs(col: Dict) -> Dict:
    col.setdefault("tableAttributes", {})
    return col["tableAttributes"]


def column_hide(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_hide  →  tableAttributes.hidden = True"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data)["hidden"] = True
        return data
    return wrapper


def column_order(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_order  →  tableAttributes.orderable = True"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data)["orderable"] = True
        return data
    return wrapper


def column_search(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_search  →  tableAttributes.searchable = False"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data)["searchable"] = False
        return data
    return wrapper

def column_null(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """@column_null  →  tableAttributes.nullable = True"""
    @wraps(fn)
    def wrapper():
        data = fn()
        _ensure_attrs(data)["nullable"] = True
        return data
    return wrapper
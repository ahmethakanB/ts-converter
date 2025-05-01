from functools import wraps
from attributes.flags.typecodes import TypeCode
from typing import Dict, Callable

def type_code(code: TypeCode):
    """@type_code(TypeCode.Decimal)"""
    def decorator(fn):
        @wraps(fn)
        def wrapped():
            data = fn()
            data["typeCode"] = int(code)
            return data
        return wrapped
    return decorator

def required(fn: Callable[[], Dict]) -> Callable[[], Dict]:
    """
    @required  →  "required": True
    """
    @wraps(fn)
    def wrapped():
        data = fn()
        data["required"] = True
        return data
    return wrapped

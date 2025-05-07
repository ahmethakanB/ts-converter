from functools import wraps
from attributes.flags.typecodes import TypeCode
from typing import Dict, Callable

def tipKodu(code: TypeCode):
    """@tipKodu(TypeCode.Int32) → listeye bir tipKoduAttribute ekler"""
    def decorator(fn):
        @wraps(fn)
        def wrapped():
            data = fn()
            attrs = data.setdefault("kolonAttributelar", [])
            attrs.append({
                "tipIsmi": "tipKoduAttribute",
                "obje": {"tipKodu": int(code)}
            })
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

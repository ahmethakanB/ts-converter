from functools import wraps
from attributes.flags.typecodes import TypeCode
from typing import Dict, Callable

def tipKodu(code: TypeCode):
    """@tipKodu(TypeCode.Int32) → data['typeCode']=9 olarak köke ekler"""
    def decorator(fn):
        @wraps(fn)
        def wrapped():
            data = fn()
            # eskiden kolonAttributelar’a ekliyordun, şimdi direk köke:
            data["typeCode"] = int(code)
            return data
        return wrapped
    return decorator

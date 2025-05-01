# attributes/flags/forms_root.py

from functools import wraps
from typing import Callable, Dict
from attributes.flags.typecodes import InputType

def input_type(input_t: InputType):
    """@input_type(InputType.text) → formAttributes.inputType"""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, mode=None, **kwargs):
            data = fn(*args, mode=mode, **kwargs)
            fa: Dict = data.setdefault("formAttributes", {})
            fa["inputType"] = int(input_t)
            return data
        return wrapper
    return decorator

def show_in(*modes: str):
    """Sadece belirtilen modlarda göster."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, mode=None, **kwargs):
            if mode not in modes:
                return None
            return fn(*args, mode=mode, **kwargs)
        return wrapper
    return decorator

def required_in(*modes: str):
    """@required_in("create") → yalnızca create modunda required"""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, mode=None, **kwargs):
            data = fn(*args, mode=mode, **kwargs)
            if mode in modes:
                fa: Dict = data.setdefault("formAttributes", {})
                fa["required"] = True
            return data
        return wrapper
    return decorator

def disabled_in(*modes: str):
    """@disabled_in("view","update") → belirtilen modlarda disabled"""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, mode=None, **kwargs):
            data = fn(*args, mode=mode, **kwargs)
            if mode in modes:
                fa: Dict = data.setdefault("formAttributes", {})
                fa["disabled"] = True
            return data
        return wrapper
    return decorator


# alias’lar kolay yazmak için
from attributes.flags.typecodes import InputType
text        = input_type(InputType.text)
textarea    = input_type(InputType.textarea)
datetime_   = input_type(InputType.datetime)
select      = input_type(InputType.select)
multiselect = input_type(InputType.multiselect)
hidden      = input_type(InputType.hidden)

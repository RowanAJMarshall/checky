from typing import Iterable, Dict, Any, Type
from itertools import zip_longest


def check(args: Iterable=(), kwargs: Dict={}, returns=None):
    """Type-check the decorated function at runtime.

    Arguments: 
    args -- an iterable of the variable types the function should take
    kwargs -- a dictionary representing any keyword arguments this function may take.
    returns -- the type returned by the decorated function.

    Raises:
    TypeCheckError -- if a checked variable does not match it's given type
    """
    def wrap(func):
        def wrapped_func(*args_actual, **kwargs_actual):

            if len(args) != len(args):
                raise Exception("WRONG")
            for pair in zip(args_actual, args):
                _check_type(*pair)

            returned = func(*args, **kwargs)
            if returns is not None and not isinstance(returned, returns):
                raise AssertionError("Returned value is not of type {}".format(returns))
            return returned
        return wrapped_func
    return wrap


def _check_type(var: Any, typ: Type) -> bool:
    if not isinstance(var, typ):
        raise AssertionError("Value <{}> is not of type {}".format(var, typ))
    return True


class TypeCheckError(TypeError):

    def __init__(self, msg):
        pass




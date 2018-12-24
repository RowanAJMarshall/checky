from typing import Iterable, Dict, Any, Type


def check(args: Iterable=(), kwargs: Dict={}, returns=None):
    """Type-check the decorated function at runtime.

    Arguments: 
    args -- an iterable of the variable types the function should take
    kwargs -- a dictionary representing any keyword arguments this function may take.
    returns -- the type returned by the decorated function.

    Raises:
    IndexError -- if the number of positional arguments nd positional argument types is not equal
    TypeCheckError -- if a checked variable does not match it's given type
    """
    def wrap(func):
        def wrapped_func(*args_actual, **kwargs_actual):
            if len(args) < len(args_actual):
                raise IndexError("Number of arguments ({}) is less than number of argument types ({})".format(len(args_actual), len(args)))
            elif len(args) > len(args_actual):
                raise IndexError("Number of arguments ({}) is more than number of argument types ({})".format(len(args_actual), len(args)))

            for pair in zip(args_actual, args):
                if not is_correct_type(*pair):
                    raise TypeCheckError("Value <{}> is not of type <{}>".format(pair[0], pair[1]))
            
            for key in kwargs.keys():
                if key in kwargs_actual and not is_correct_type(kwargs_actual[key], kwargs[key]):
                    raise TypeCheckError("Value <{}> is not of type <{}>".format(kwargs[key], kwargs_actual[key]))

            returned = func(*args, **kwargs)
            if returns is not None and not isinstance(returned, returns):
                raise TypeCheckError("Returned value <{}> is not of type <{}>".format(returned, returns))

            return returned
        return wrapped_func
    return wrap


def is_correct_type(var: Any, typ: Type) -> bool:
    return isinstance(var, typ)


class TypeCheckError(TypeError):
    def __init__(self, msg):
        sum.__init__(msg)




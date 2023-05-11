#!/usr/bin/python 

# Could also use NoneType = type(None) which is exactly the same
# but felt like this is the right way since it's the built-in
# library for this exact purpose and only a single type is imported.

from types import NoneType 

# Since the code is hard to understand by it's own,
# type hinting is even more important in this case.

from typing import Callable,Any


def handler(*call: Callable[...,Any], 
            **callable_kwds: tuple[tuple[Any] | None, dict[str,Any] | None]
            ) -> dict[str,Any]:
    
    _returns = {}

    for _call in call:

        if not callable(_call):
            raise TypeError(f"{_call} is not a callable object")
        
        callable_name = _call.__name__
        _args, _kwds = (), {}

        if callable_name in callable_kwds.keys():

            _all_args = callable_kwds[callable_name]

            if not isinstance(_all_args[0], (tuple,NoneType)):
                raise TypeError(f"Got {type(_all_args[0])} instead of tuple[args] or None as positional arguments")
            _args = () if _all_args[0] is None else _all_args[0]

            if not isinstance(_all_args[1], (dict,NoneType)):
                raise TypeError(f"Got {type(_all_args[1])} instead of dict[argname, args] or None as keyword arguments")
            _kwds = {} if _all_args[1] is None else _all_args[1]

        _returned = _call(*_args, **_kwds)

        _returns.update({callable_name:_returned})

    return _returns

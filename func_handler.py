from typing import Callable,Any

def handler(*func: Callable[...,Any], **func_kwds: dict[str,Any] | tuple[Any]) -> dict[str,Any]:
    _returns = {}
    for _func in func:
        _funcname = _func.__name__
        if _funcname in func_kwds.keys():
            _args = func_kwds[_funcname]
            if type(_args) == tuple: #positional arguments
                _returned = _func(*_args)
            elif type(_args) == dict: #keyword arguments
                _returned = _func(**_args)
        else:
            _returned = _func()
        _returns.update({_func.__name__ : _returned})
    return _returns

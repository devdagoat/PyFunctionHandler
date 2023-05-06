from typing import Callable,Any

def handler(*func: Callable[...,Any], **func_kwds: dict[str,Any] | tuple[Any]) -> dict[str,Any]:
    __returns = {}
    for __func in func:
        if __func.__name__ in func_kwds.keys():
            __args = func_kwds[__func.__name__]
            if type(__args) == tuple: #positional arguments
                __returned = __func(*__args)
            elif type(__args) == dict: #keyword arguments
                __returned = __func(**__args)
        else:
            __returned = __func()
        __returns.update({__func.__name__ : __returned})
    return __returns

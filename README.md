# PyFunctionHandler
Handler function written in Python that executes other functions with given args (positional and keyword) in one go.
## Usage
Just add the function and imports to your code really
## Explanation
```python
from typing import Callable,Any # type hinting is important!

# func: Callable, can take any amount of arguments and can return anything
# func_kwds: {function name : any arguments in tuple or dict depending on arg type}

def handler(*func: Callable[...,Any], **func_kwds: dict[str,Any] | tuple[Any]) -> dict[str,Any]:
    _returns = {} # initialize dict to be returned
    for _func in func: # iterate through callables
        _funcname = _func.__name__ # define _funcname
        if _funcname in func_kwds.keys(): # check if args are given
            _args = func_kwds[_funcname] # define args from keyword args dict
            if type(_args) == tuple: # positional arguments 
                _returned = _func(*_args) # pass accordingly and save returned value
            elif type(_args) == dict: # keyword arguments
                _returned = _func(**_args) # pass accordingly and save returned value
        else:
            _returned = _func() # call without args since none is given
        _returns.update({_func.__name__ : _returned}) # function name : returned object
    return _returns # return the dict
```

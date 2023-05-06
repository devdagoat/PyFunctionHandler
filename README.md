# PyFunctionHandler
Handler function written in Python that executes other functions with given args (positional and keyword) in one go.
## Usage
Just add the function and imports to your code really
## Explanation
```python
from typing import Callable,Any #type hinting is important!

# func: Callable, can take any amount of arguments and can return anything
# func_kwds: {function name : any arguments in tuple or dict depending on arg type}

def handler(*func: Callable[...,Any], **func_kwds: dict[str,Any] | tuple[Any]) -> dict[str,Any]:
    __returns = {} # initialize dict to be returned
    for __func in func: # iterate through every func that has passed through
        if __func.__name__ in func_kwds.keys(): # check if an arg is passed
            __args = func_kwds[__func.__name__] # set __args variable to value of function name
            if type(__args) == tuple: # positional arguments
                __returned = __func(*__args) # call the function, pass args as positional args then return the value if any
            elif type(__args) == dict: # keyword arguments
                __returned = __func(**__args) # call the function, pass args as keyword args then return the value if any
        else:
            __returned = __func() # do not pass any args since none is given
        __returns.update({__func.__name__ : __returned}) # {function name : returned object from that function}
    return __returns
```

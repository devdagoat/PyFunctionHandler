# PyFunctionHandler
Handler function written in Python that executes other functions with given args (positional and keyword) in one go.
## Usage
```
handler(func, func=(
(positional arg1, positional arg2, ...) or None, 
{keyword arg1 name: keyword arg1, ...} or None
)
```
## Explanation
```python
from types import NoneType 

# Since the code is hard to understand by it's own,
# type hinting is even more important in this case.

from typing import Callable,Any


def handler(*call: Callable[...,Any], 
            **callable_kwds: tuple[tuple[Any] | None, dict[str,Any] | None]
            ) -> dict[str,Any]:
    
    _returns = {} # Initialize dict to be returned

    for _call in call:

        if not callable(_call): # Check if object is callable
            raise TypeError(f"{_call} is not a callable object")
        
        callable_name = _call.__name__ # Set callable name variable
        _args, _kwds = (), {} # Set default args

        if callable_name in callable_kwds.keys(): # If an argument is passed:

            _all_args = callable_kwds[callable_name]

            if not isinstance(_all_args[0], (tuple,NoneType)): # Check if positional arguments are valid
                raise TypeError(f"Got {type(_all_args[0])} instead of tuple[args] or None as positional arguments")
            _args = () if _all_args[0] is None else _all_args[0]

            if not isinstance(_all_args[1], (dict,NoneType)): # Check if keyword arguments are valid
                raise TypeError(f"Got {type(_all_args[1])} instead of dict[argname, args] or None as keyword arguments")
            _kwds = {} if _all_args[1] is None else _all_args[1]

        _returned = _call(*_args, **_kwds) # Call the callable with arguments and save returned object

        _returns.update({callable_name : _returned}) # Update dict with the items

    return _returns
```

## Testing
```python

def a():
    return "No args are passed to this function"

def x(a:int, b:int) -> int:
    return a ** b

def y(a:int, b:int) -> float:
    return a / b
    
def z(a:int, b:int, p:int) -> int:
    return (a+b) ** p

# Lambdas are unsupported because they don't have any name to begin with! 

l = lambda i: i*1000 

# It's possible to use them if their __name__ is explicitly set,
# but don't do this unless you absolutely have to.

l.__name__ = "l"

# Instances can be created with the handler as well:

class MyClass:
    def __init__(self,s1:str,s2:str) -> None:
        self.s1 = s1
        self.s2 = s2
    def combine(self,s3:str) -> str:
        return self.s1 + self.s2 + s3
    
my_instance = MyClass("Hi, ", "I am ")


returns = handler(a, x, y, z, MyClass, my_instance.combine, print, str, 
                  x=((3, 5), None), # positional args
                  y=(None, {"a":3, "b":4}), # keyword args
                  z=((2, 10), {"p":2}), # mixed args
                  MyClass=(("Hi, ", "this is a test"), None), # positional args passed to class
                  combine=(None, {"s3":"Me!"}), # note that we use the function name only
                  print=(("Print function always returns None",), None), # print can only accept positional args
                  str=(None, {"object":42})) # it's possible to pass object as kwargs to str type

print(returns)

```
## What cannot be done
- can't pass lambda functions, unless \_\_name\_\_ is explicitly set
- can't pass callable instances (instances of classes that have a \_\_call\_\_ method), similar issues with above, instances don't have a \_\_name\_\_ attribute and even if that was handled, the name of the method (\_\_call\_\_) isn't unique by any means.

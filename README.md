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

## Testing
```python
def x(a:int,b:int) -> int:
    return a**b

def y(a:int,b:int) -> float:
    return a/b
    
# lambdas are unsupported because they don't have any name to begin with! 

l = lambda i: i*1000 

# it's possible if the __name__ is explicitly set, but don't do it unless you absolutely have to. It's not Pythonic at all  

l.__name__ = "l"

# instances can be created as well:

class MyClass:
    def __init__(self,s1:str,s2:str) -> None:
        self.s1 = s1
        self.s2 = s2
    def combine(self,s3:str) -> str:
        return self.s1 + self.s2 + s3
    
my_instance = MyClass("Hi, ", "I am ")

returns = handler(x, y, MyClass, my_instance.combine, print, str, 
                  x=(3,5), # positional args 
                  y={"a":10,"b":4}, # keyword args
                  MyClass=("Hi, ","this is a test"), # positional args passed to class
                  combine={"s3":"Me!"}, # note that we use the function name only
                  print=("Print function returns None",), # print can only accept positional args
                  str={"object":42}) # built-in type that returns a string

print(returns) # prints the following: {'x': 243, 'y': 2.5, 'MyClass': <__main__.MyClass object at <address in memory>>, 'combine': 'Hi, I am Me!', 'print': None, 'str': '42'}

# and if we want to use the values:

other_instance = returns["MyClass"]
result_y = returns["y"]
print(other_instance.combine("!!!!!")) # prints: Hi, this is a test!!!!!
print(result_y) # prints: 2.5
```
## What cannot be passed
- lambda functions, unless \_\_name\_\_ is explicitly set
- callable instances (instances of classes that have a \_\_call\_\_ method), similar issues with above, instances don't have a \_\_name\_\_ attribute and even if that was handled, the name of the method (\_\_call\_\_) isn't unique by any means.

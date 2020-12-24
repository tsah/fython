# fython
Functional utilities for Python, inspired by Scala

## FOptional
```python
from fython import option

def my_function():
    return (option(something_that_might_return_none())
            .map(do_something)
            .map(do_another_thing)
            .get_or_else(default_value))

@dataclass
class Inner:
    v: Optional[str]

@dataclass
class Outer:
    inner: Optional[Inner]

c = Outer(Inner("hello"))    

inner_value = (option(c)
               .flatmap(lambda c: c.inner)
               .flatmap(lambda inner: inner.v)
               .get_or_throw())
```
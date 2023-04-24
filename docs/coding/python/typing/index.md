# Python Typing

Simple typing syntax for Python variables, functions and classes with the `typing` library.

```python
from typing import ...
```

-   [https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)

!!! note

    For more specific data validation, use Pydantic models.

    -  [https://docs.pydantic.dev/](https://docs.pydantic.dev/)

    ```terminal
    pip install pydantic
    ```

## Function Inputs

**Easy Usage**

```python
def add(a: int, b: int) -> int:
    return a + b
```

-   `a`, `b` are `int` type
-   `func` returns `int` type

**Lists / Dicts**

```python
def process(items: list[int]):
    pass
```

-   `items` is a `list` of `int` type

```python
def process(items: dict[str, int]):
    pass
```

-   `items` is a `dict` with `str` keys and `int` values

**Optional**

```python
from typing import Optional

def process(a: int, b: Optional[int] = 0):
    pass
```

-   `b` is optional and defaults to `0`

**Union**

```python
from typing import Union

def process(a: Union[int, str]):
    pass
```

-   `a` can be `int` or `str` type

## Function Outputs

**Return Values**

```python
def process() -> list[int]:
    return [1, 2, 3]
```

-   `process` returns a `list` of `int` type

```python
def process() -> tuple[str, int]:
    return 'a', 1
```

-   `process` returns a `tuple` of `str` and `int` type

**Return None**

```python
def process() -> None:
    pass
```

-   `process` returns `None`

## Classes

**Class Attributes**

```python
class A:
    def __init__(self, a: int):
        self.a = a

def process(a: A):
    pass
```

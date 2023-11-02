---
icon: material/toy-brick-plus-outline
---

# enum

!!! note

    Enumerations are a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

-   [`enum` Documentation :material-file-document-arrow-right-outline:](https://docs.python.org/3/library/enum.html){target="\_blank"}

## Defining an Enumeration

Each member of an enum needs an assigned value. Values can be different types.

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 4
    WHITE = 5
```

### `enum.auto()` Function

This generates unique values for each member of the enumeration.

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    BLACK = auto()
    WHITE = auto()
```

## Accessing Members

```python
Color.RED
Color.RED.name
Color.RED.value
Color["RED"]
```

```text
Color.RED
'RED'
1
Color.RED: 1
```

### Iteration

```python
for color in Color:
    print(color)
```

```text
Color.RED
Color.GREEN
Color.BLUE
...
```

### Comparing Members

```python
Color.RED is Color.RED
Color.RED is Color.GREEN
```

```text
True
False
```

## Flags

Flag-Enums are used to define a set of flags for another member.

> For example, a user may have `READ`, `WRITE`, `EXECUTE`, and `DELETE` access rights. These can be combined into a
> single `ADMIN` flag.

```python
from enum import Flag, auto

class AccessRights(Falg):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    DELETE = auto()
    ADMIN = READ | WRITE | EXECUTE | DELETE
```

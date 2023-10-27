---
icon: material/alphabetical-variant
---

# abc

!!! info "Abstract Base Classes"

    Abstract base classes are standardized way to define interfaces in Python. They are used to define a minimal set of methods that a class must implement in order to be considered a duck type of the abstract base class.

[Python `abc` Documentation :material-file-document-arrow-right-outline:](https://docs.python.org/3/library/abc.html){ .md-button target="\_blank"}

## Abstract Base Class Usage

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

The `Animal` class inherits from `ABC` and not from the `object` class. `@abstractmethod` decorator marks the `speak` method as abstract. Any class that inherits from `Animal` must implement the `speak` method.

### Inheriting from an Abstract Base Class

```python
class Cat(Animal):
    def speak(self):
        print('Meow')
```

```text
>>> issubclass(Cat, Animal)
True

>>> cat = Cat()
>>> cat.speak()
Meow
```

**Implementing no `speak` method**

```python
class Dog(Animal):
    def __init__(self, name):
        self.name = name
```

```text
>>> dog = Dog('Buddy')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

TypeError: Can't instantiate abstract class Dog with abstract methods speak
```

## Abstract Properties

```python
from abc import ABC, abstractproperty

class Animal(ABC):
    @abstractproperty
    def name(self):
        pass
```

The `Animal` class has an abstract property `name`. Any class that inherits from `Animal` must implement the `name` property.

```python
class Dog(Animal):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```

```text
>>> dog = Dog('Buddy')
>>> dog.name
'Buddy'

>>> dog.name = 'Buddy Jr.'
>>> dog.name
'Buddy Jr.'
```

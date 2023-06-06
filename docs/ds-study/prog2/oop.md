# Python Classes & Objects

!!! info

    Classes are blueprints for objects. Objects are instances of classes. Classes can be used to create multiple objects.

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print("Driving a", self.color, self.model)
```

```python
ferrari = Car("red", "Ferrari")
audi = Car("blue", "Audi")

ferrari.drive()
audi.drive()

# Output:
# >>> Driving a red Ferrari
# >>> Driving a blue Audi
```

**Important to know:**

-   `self` is a reference to the current instance of the class
-   `self` comes always first in the method definition
-   `__init__` is the constructor of the class (see more [here](#__init__))
-   `__init__` is called when an object is created (after `__new__`)
-   All classes inherit from `object` by default

## Arguments

### Optional Arguments

!!! info

    Optional arguments can be used to set default values for attributes.

```python hl_lines="2 5"
class Car:
    def __init__(self, color, model, battery=0):
        self.color = color
        self.model = model
        self.battery = battery

    def drive(self):
        print("Driving a", self.color, self.model, "with", self.battery, "kWh")
```

```python hl_lines="1 8"
car = Car("red", "Ferrari")
e_car = Car("green", "Tesla", 100)

car.drive()
e_car.drive()

# Output:
# >>> Driving a red Ferrari with 0 kWh
# >>> Driving a green Tesla with 100 kWh
```

### Positional Arguments

!!! info

    Positional arguments can be used to set attributes in the order they are defined in the class.

```python hl_lines="2"
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print("Driving a", self.color, self.model)
```

```python hl_lines="1"
car = Car("red", "Ferrari")
car.drive()

# Output:
# >>> Driving a red Ferrari with 0 kWh
```

### Keyword Arguments

!!! info

    Keyword arguments can be used to set attributes in any order accessible by their keyname.

```python hl_lines="2"
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print("Driving a", self.color, self.model)
```

```python hl_lines="1"
car = Car(model="Ferrari", color="red")
car.drive()

# Output:
# >>> Driving a red Ferrari with 0 kWh
```

### `*args` & `**kwargs`

!!! info

    `*args` and `**kwargs` can be used to pass a variable number of arguments to a function like a list or a dictionary.

    -   `*args` is used to pass a variable number of **positional** arguments (arguments without a keyname)
    -   `**kwargs` is used to pass a variable number of **keyword** arguments (arguments with a keyname)

```python hl_lines="1 2 4"
def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
```

```python
print_args_and_kwargs("Hello", "World", name="John", age=42)

# Output:
# >>> Hello
# >>> World
# >>> name John
# >>> age 42
```

## Attributes

### Object Attributes

!!! info

    Object attributes are attributes that are defined in the `__init__` method. They are unique for each instance of the class.

```python hl_lines="2 3 4"
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print("Driving a", self.color, self.model)
```

```python
car = Car("red", "Ferrari")
print(car.color)
print(car.model)

# Output:
# >>> red
# >>> Ferrari
```

### Class Attributes

!!! info

    Class attributes are attributes that are defined outside of the `__init__` method. They are shared between all instances of the class.

```python hl_lines="2 7"
class Car:
    total_cars = 0

    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.total_cars += 1

    def drive(self):
        print("Driving a", self.color, self.model)
```

```python hl_lines="3"
car1 = Car("red", "Ferrari")
car2 = Car("blue", "Ferrari")
print(Car.total_cars)

# Output:
# >>> 2
```

### Semi-Private Attributes

!!! info

    Semi-private attributes are attributes that are defined with a single underscore `_` in front of the attribute name. They can be accessed from outside the class but should not be accessed. This is just a convention for developers to know that these attributes are for internal use only.

```python hl_lines="2 5"
class Car:
    def __init__(self, color, model, secret):
        self.model = model
        self.color = color
        self._secret = secret

    def get_secret(self):
        return self._secret

    def set_secret(self, secret):
        self._secret = secret
```

```python
car = Car("blue", "Ferrari", "secret")
print(car.get_secret())
print(car._secret)

# Output:
# >>> secret
# >>> secret
```

### Private Attributes

!!! info

    Private attributes are attributes that are defined with a double underscore `__` in front of the attribute name. They can only be accessed from within the class. This is used to prevent accidental access from outside the class.

```python hl_lines="5 7 8 10 11"
class Car:
    def __init__(self, color, model, secret):
        self.model = model
        self.color = color
        self.__secret = secret

    def get_secret(self):
        return self.__secret

    def set_secret(self, secret):
        self.__secret = secret
```

```python
car = Car("blue", "Ferrari", "secret")
print(car.get_secret())
print(car.__secret)

# Output:
# >>> secret
# >>> AttributeError: 'Car' object has no attribute '__secret'
```

### Property Attributes

!!! info

    Property attributes are attributes that are defined with the `@property` decorator. They are used to access private attributes from outside the class. By using the `@property` decorator, the private attribute can be accessed like a normal attribute. By using the `@attribute.setter` decorator, the private attribute can be modified like a normal attribute.

```python hl_lines="5 7 11"
class Car:
    def __init__(self, color, model, secret):
        self.model = model
        self.color = color
        self.__secret = secret

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, value):
        self.__secret = value
```

```python
car = Car("blue", "Ferrari", "secret")
car.secret
car.secret = "new secret"
car.secret

# Output:
# >>> secret
# >>> new secret
```

## Methods

### `__new__`

!!! info

    The `__new__` method is called **before** an object is created. It is used to modify the object during creation.

```python
class Car:
    def __new__(cls, color, model):
        if color == "red":
            return super().__new__(cls)
        else:
            return None

    def __init__(self, color, model):
        self.color = color
        self.model = model
```

```python
car = Car("red", "Ferrari")
car = Car("blue", "Ferrari")

print(car.color)
print(car)

# Output:
# >>> red
# >>> None
```

### `__init__`

!!! info

    The `__init__` method is called **when** an object is created. It is used to initialize the object's attributes and methods.

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
```

```python
car = Car("red", "Ferrari")

print(car.color)

# Output:
# >>> red
```

### `__str__` & `__repr__`

!!! info

    - The `__str__` method is called when the object is printed. It should return a string representation of the object.
    - The `__repr__` method is called when the object is printed in the console. It should return a string representation of the object.

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def __str__(self):
        return "Car(color={}, model={})".format(self.color, self.model)

    def __repr__(self):
        return "Car(color={}, model={})".format(self.color, self.model)
```

```python
car = Car("red", "Ferrari")

print(car) # This will call __str__
car # This will call __repr__

# Output:
# >>> Car(color=red, model=Ferrari)
# >>> Car(color=red, model=Ferrari)
```

### `@abstractmethod`

!!! info

    The `@abstractmethod` decorator is used to define abstract methods. Abstract methods are methods that are not implemented in the class but must be implemented in the subclass.

```python hl_lines="8 9 10 13 14"
from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    def __init__(self, color, model):
        self.color = color
        self.model = model

    @abstractmethod
    def drive(self):
        pass

class Ferrari(Car):
    def drive(self):
        print("Driving a", self.color, self.model)
```

```python
car = Car("red", "Ferrari")

# Output:
# >>> TypeError: Can't instantiate abstract class Car with abstract methods drive
```

```python
ferrari = Ferrari("red", "Ferrari")
ferrari.drive()

# Output:
# >>> Driving a red Ferrari
```

### `@staticmethod`

!!! info

    The `@staticmethod` decorator is used to define static methods. Static methods are methods that do not require an instance of the class to be called. They are usually used to create utility functions which are belonging to a class thematically.

```python hl_lines="6 7 8"
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    @staticmethod
    def drive():
        print("Driving a car")
```

```python
car = Car("red", "Ferrari")
car.drive()

# Output:
# >>> Driving a car
```

### `@classmethod`

!!! info

    The `@classmethod` decorator is used to define class methods. Class methods are methods that are bound to the class and not to an instance of the class. They are usually used to create factory methods which are used to create an instance of the class.

```python hl_lines="9 10 11"
class Car:
    total_cars = 0

    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
```

```python
car1 = Car("red", "Ferrari")
car2 = Car("blue", "Ferrari")

print(Car.get_total_cars())

# Output:
# >>> 2
```

## Concepts

The following concepts are important to understand object-oriented programming. They are not specific to Python. They are also used in other oop languages like Java.

### Abstraction

!!! info

    Abstraction means that only the relevant information is shown to the user. The user does not need to know the internal details of the object.

```python
class Car:
    def __init__(self, color, model, key):
        self.color = color
        self.model = model
        self.__key = key

    def drive(self):
        if self.__key == True:
            print("Driving a", self.color, self.model)
        else:
            print("You need the correct key to drive this car")

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key
```

```python
car = Car("red", "Ferrari", True)

car.drive()
car.set_key(False)
car.drive()

# Output:
# >>> Driving a red Ferrari
# >>> You need the correct key to drive this car
```

### Encapsulation

!!! info

    Encapsulation means that the internal representation of an object is hidden from the outside. Only the object itself can access and modify its internal state.

```python
class Car:
    def __init__(self, color, model):
        self.__color = color
        self.__model = model

    def drive(self):
        print("Driving a", self.__color, self.__model)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
```

```python
car = Car("yellow", "VW")

car.drive()
car.set_color("orange")
car.drive()

# Output:
# >>> Driving a yellow VW
# >>> Driving a orange VW
```

### Inheritance

!!! info

    Classes can inherit from other classes. The child class inherits all attributes and methods from the parent class.

!!! warning

    Methods and attributes can be overwritten in the child class. The parent class is not affected.

```python
class ElectricCar(Car):
    def __init__(self, color, model, battery):
        super().__init__(color, model)
        self.battery = battery

    def charge(self):
        print("Charging", self.color, self.model, "with", self.battery, "kWh")
```

```python
car = ElectricCar("green", "Tesla", 100)
car.drive()

# Output:
# >>> Driving a green Tesla with 100 kWh
```

### Polymorphism

!!! info

    Polymorphism means that the same method can be used for different types of objects. The method will behave differently depending on the type of object.

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print("Driving a", self.color, self.model)

class ElectricCar(Car):
    def __init__(self, color, model, battery):
        super().__init__(color, model)
        self.battery = battery

    def drive(self):
        print("Driving a", self.color, self.model, "with", self.battery, "kWh")
```

```python
car = Car("red", "Ferrari")
e_car = ElectricCar("green", "Tesla", 100)

car.drive()
e_car.drive()

# Output:
# >>> Driving a red Ferrari
# >>> Driving a green Tesla with 100 kWh
```

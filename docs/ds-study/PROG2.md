# PROG2

Notes for the PROG2 course in my bachelor's degree program Data Science at ZHAW.

## Python Classes & Objects

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

### Arguments

#### Optional Arguments

!!! info

    Optional arguments can be used to set default values for attributes.

```python
class Car:
    def __init__(self, color, model, battery=0):
        self.color = color
        self.model = model
        self.battery = battery

    def drive(self):
        print("Driving a", self.color, self.model, "with", self.battery, "kWh")
```

```python
car = Car("red", "Ferrari")
e_car = Car("green", "Tesla", 100)

car.drive()
e_car.drive()

# Output:
# >>> Driving a red Ferrari with 0 kWh
# >>> Driving a green Tesla with 100 kWh
```

#### Positional Arguments

!!! info

    Positional arguments can be used to set attributes in the order they are defined in the class.

```python
class Car:
    def __init__(self, color, model, battery=0):
        self.color = color
        self.model = model
        self.battery = battery

    def drive(self):
        print("Driving a", self.color, self.model, "with", self.battery, "kWh")
```

```python
car = Car("red", "Ferrari")
car.drive()

# Output:
# >>> Driving a red Ferrari with 0 kWh
```

#### Keyword Arguments

!!! info

    Keyword arguments can be used to set attributes in any order accessible by their keyname.

```python
class Car:
    def __init__(self, color, model, battery=0):
        self.color = color
        self.model = model
        self.battery = battery

    def drive(self):
        print("Driving a", self.color, self.model, "with", self.battery, "kWh")
```

```python
car = Car(model="Ferrari", color="red")
car.drive()

# Output:
# >>> Driving a red Ferrari with 0 kWh
```

#### `*args` & `**kwargs`

!!! info

    `*args` and `**kwargs` can be used to pass a variable number of arguments to a function like a list or a dictionary.

    -   `*args` is used to pass a variable number of **positional** arguments
    -   `**kwargs` is used to pass a variable number of **keyword** arguments

```python
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

### Methods

#### `__new__`

!!! info

    The `__new__` method is called when an object is created. It is used to modify the object during creation.

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

#### `__init__`

!!! info

    The `__init__` method is called when an object is created. It is used to initialize the object's attributes and methods.

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

#### `__str__` & `__repr__`

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

#### `@abstractmethod`

!!! info

    The `@abstractmethod` decorator is used to define abstract methods. Abstract methods are methods that are not implemented in the class but must be implemented in the subclass.

```python
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

#### `@staticmethod`

!!! info

    The `@staticmethod` decorator is used to define static methods. Static methods are methods that do not require an instance of the class to be called. They are usually used to create utility functions which are belonging to a class thematically.

```python
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

#### `@classmethod`

!!! info

    The `@classmethod` decorator is used to define class methods. Class methods are methods that are bound to the class and not to an instance of the class. They are usually used to create factory methods which are used to create an instance of the class.

```python
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

### Concepts

The following concepts are important to understand object-oriented programming. They are not specific to Python. They are also used in other oop languages like Java.

#### Abstraction

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

#### Encapsulation

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

#### Inheritance

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

#### Polymorphism

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

---

## Testing

!!! info

    Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not.

Widely used testing frameworks for Python:

-   [unittest](https://docs.python.org/3/library/unittest.html)
-   [pytest](https://docs.pytest.org/en/latest/)
-   [nose](https://nose.readthedocs.io/en/latest/)

### Unit Testing

!!! info

    Unit testing is a software testing method by which individual units of source code are tested to determine whether they are fit for use.

```python
def add(x, y):
    return x + y
```

```python
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)
        self.assertEqual(add(1, 4), 5)

if __name__ == "__main__":
    unittest.main()
```

### Mocking

!!! info

    Mocking is a process used in unit testing when the unit being tested has external dependencies. The purpose of mocking is to isolate and focus on the code being tested and not on the behavior or state of external dependencies.

```python
import unittest
from unittest.mock import patch

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    @patch("__main__.add")
    def test_add(self, mock_add):
        mock_add.return_value = 5
        self.assertEqual(add(1, 2), 5)
        self.assertEqual(add(1, 3), 5)
        self.assertEqual(add(1, 4), 5)

if __name__ == "__main__":
    unittest.main()
```

### Coverage

!!! info

    Code coverage is a measure used to describe the degree to which the source code of a program is tested by a particular test suite.

```python
def add(x, y):
    if x > 0:
        return x + y
    else:
        return y
```

```python
import unittest
import coverage

cov = coverage.Coverage()
cov.start()

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)
        self.assertEqual(add(1, 4), 5)

if __name__ == "__main__":
    unittest.main()
    cov.stop()
    cov.save()
    cov.report()
```

### Non-Functional Testing

!!! info

    Non-functional testing is the testing of a software application or system for its non-functional requirements: the way a system operates, rather than specific behaviours of that system.

-   Execution Time
-   System Resources (CPU, Memory, Disk, Network)
-   Refactoring (lines of code, cyclomatic complexity, syntax complexity)

---

## Pandas

!!! info

    Pandas is a Python library for data analysis and manipulation. It provides data structures and functions to work with structured data like CSV files, Excel sheets or SQL tables.

### Load & Save Data

```python
import pandas as pd

# Load data
df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1", engine="openpyxl")

# Save data
df.to_csv("data.csv", sep=";", encoding="utf-8", index=False)
```

**Note:**

-   `sep` is the separator used in the CSV file (default is `,`)
-   `encoding` is the encoding used in the CSV file (default is `utf-8`)
    -   `utf-8`
    -   `latin-1`
    -   see [here](https://docs.python.org/3/library/codecs.html#standard-encodings) for a list of all encodings

Web

```python
import pandas as pd

url = "https://example.com/data.csv"
df = pd.read_csv(url, sep=";", encoding="utf-8")
```

SQL

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM data", conn)
```

### Column Operations

Select Columns

```python
df2 = df[["column1", "column2"]]
```

Drop Columns

```python
df = df.drop(columns=["column1", "column2"])
```

Rename Column

```python
df = df.rename(columns={"old": "new"})
```

Apply to Column

```python
df["column"] = df["column"].apply(lambda x: x + 1)
```

Add Columns

```python
df["new"] = df["column1"] + df["column2"]
```

Remove Duplicates

```python
df = df.drop_duplicates(subset="column")
```

### Row Operations

Filter Rows

```python
df = df[df["column"] > 10]
```

Group Rows

```python
df = df.groupby("column").sum()
```

Sort Rows

```python
df = df.sort_values("column", ascending=False)
```

Select Rows and Columns

```python
df = df.loc[df["column"] > 10, ["column1", "column2"]]
```

Iterate over Rows

```python
for index, row in df.iterrows():
    print(index, row["column1"], row["column2"])
```

---

## Internet Standards & Encodings

### URL Encoding

```python
b'Dor\xc3\xa9naz'.decode("utf-8")

# Output:
# >>> 'Dorénaz'
```

```python
import urllib.parse as urlparse
urlparse.quote("%*")
# Output:
# >>> '%25%2A'

urlparse.urlencode({"name": "Dorénaz"})
# Output:
# >>> 'name=Dor%C3%A9naz'
```

### Date & Time Formats

| Name            | Format                            | Example                         |
| --------------- | --------------------------------- | ------------------------------- |
| UNIX Time       | `int`                             | 1571081990                      |
| ISO 8601        | `YYYY-MM-DD hh:mm:ss.ss`          | 2019-10-14T12:33:10+00:00       |
| RFC 3339        | `YYYY-MM-DDThh:mm:ss.sssZ`        | 2019-10-14T12:33:10.000Z        |
| RFC (2)822/5322 | `ddd, DD MMM YYYY hh:mm:ss +zzzz` | Mon, 14 Oct 2019 12:33:10 +0000 |
| RFC 7231        | `ddd, DD MMM YYYY hh:mm:ss GMT`   | Mon, 14 Oct 2019 12:33:10 GMT   |

### HTTP & URI

#### URI Formats

| Name                    | Example                                                               |
| ----------------------- | --------------------------------------------------------------------- |
| URI / URL               | `https://www.example.com:8080/path/to/resource?query=string#fragment` |
| IRI / IRL               | `http://localhost/api/products/تلفاز`                                 |
| URI Template (RFC 6570) | `https://www.example.com/{version}/path/to/{resource}`                |
| Ressource Formats       | `html`, `json`, `yaml`, `xml`, `binary`, `text`                       |

#### HTTP Methods

| Name   | Description                                            |
| ------ | ------------------------------------------------------ |
| GET    | Requests a representation of the specified resource    |
| POST   | Submits data to be processed to the specified resource |
| PUT    | Uploads a representation of the specified resource     |
| DELETE | Deletes the specified resource                         |

#### HTTP Status Codes

Scheme:

| Code | Name          | Description                                                    |
| ---- | ------------- | -------------------------------------------------------------- |
| 1xx  | Informational | Request received, continuing process                           |
| 2xx  | Success       | The action was successfully received, understood, and accepted |
| 3xx  | Redirection   | Further action must be taken in order to complete the request  |
| 4xx  | Client Error  | The request contains bad syntax or cannot be fulfilled         |
| 5xx  | Server Error  | The server failed to fulfill an apparently valid request       |

Most common:

| Code | Name        | Description                                                                             |
| ---- | ----------- | --------------------------------------------------------------------------------------- |
| 100  | Continue    | The server has received the request headers, and the client should proceed              |
| 200  | OK          | Standard response for successful HTTP requests                                          |
| 201  | Created     | The request has been fulfilled, resulting in the creation of a new resource             |
| 202  | Accepted    | The request has been accepted for processing, but the processing has not been completed |
| 400  | Bad Request | The server cannot or will not process the request due to an apparent client error       |
| 404  | Not Found   | The requested resource could not be found but may be available in the future            |
| ...  | ...         | ...                                                                                     |

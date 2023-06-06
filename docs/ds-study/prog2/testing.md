# Testing

!!! info

    Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not.

Widely used testing frameworks for Python:

-   [unittest](https://docs.python.org/3/library/unittest.html)
-   [pytest](https://docs.pytest.org/en/latest/)
-   [nose](https://nose.readthedocs.io/en/latest/)

## Unit Testing

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

## Mocking

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

## Coverage

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

## Non-Functional Testing

!!! info

    Non-functional testing is the testing of a software application or system for its non-functional requirements: the way a system operates, rather than specific behaviours of that system.

-   Execution Time
-   System Resources (CPU, Memory, Disk, Network)
-   Refactoring (lines of code, cyclomatic complexity, syntax complexity)

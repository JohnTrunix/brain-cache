# Pickle

Pickle is a standard Python module for serializing and deserializing Python objects. It is used to save objects to a file and load them back later.

!!! warning "Warning"

    Pickle is not secure. Never unpickle data received from an untrusted or unauthenticated source.

## Pickle vs JSON

-   Pickle is a binary format, while JSON is a text format
-   Pickle is more efficient than JSON
-   Pickle is not human-readable
-   Pickle is not secure (can execute arbitrary code)

## Example

```python
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.name}, {self.age})'

person = Person('John', 30)
```

Save the object to a file:

```python
with open('person.pickle', 'wb') as f:
    pickle.dump(person, f)
```

Load the object from a file:

```python
with open('person.pickle', 'rb') as f:
    person = pickle.load(f)
```

!!! tip "Tip"

    Use `cPickle` instead of `pickle` for better performance (C implementation up to 1000 times faster)

!!! example "See also"

    Example Notebook: [pickle.ipynb](../../examples/python/pickles.ipynb)

## Multiple Objects

```python
import pickle

p1 = Person('John', 30)
p2 = Person('Jane', 25)

with open('people.pickle', 'wb') as f:
    pickle.dump(p1, f)
    pickle.dump(p2, f)
```

Load the objects from a file in the same order:

```python
with open('people.pickle', 'rb') as f:
    p1 = pickle.load(f)
    p2 = pickle.load(f)
```

### Pickle DataFrames

=== "pickles"

    ```python
    data = {}
    data['df1'] = df1
    data['df2'] = df2

    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)

    data1 = data['df1']
    data2 = data['df2']
    ```

=== "pandas"

    ```python
    df1.to_pickle('df1.pickle')
    df2.to_pickle('df2.pickle')

    df1 = pd.read_pickle('df1.pickle')
    df2 = pd.read_pickle('df2.pickle')
    ```

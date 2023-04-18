# FastAPI Parameters

Path parameter in decorator, gets executed wenn call is made to `'/'` with `get` method.

```python
@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

## Path Parameters

Path variables are defined in the path of the decorator with `{}`.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

### Validation with Type Hints

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

-   `{item_id} = 1` results `{"item_id": 1}`
-   `{item_id} = "foo"` results `type_error.integer`

!!! warning "Warning: Order matters"

    `/users/me` has to be defined before `/users/{user_id}`

### Predefined Values

```python
from enum import Enum

class Name(str, Enum):
    a = "a"
    b = "b"

@app.get("/models/{name}")
def get(name: Name):
    if name == Name.a:
        return {"name": name, "value": "a"}
    if name == Name.b:
        return {"name": name, "value": "b"}
    return {"name": name, "value": "unknown"}
```

### Path Parameter Converter

!!! note

    If the path has no other parameters `{}`, just the path use `:path`

```python
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
```

## Query Parameters

Other function parameters are interpreted as query parameters.

```terminal
http://127.0.0.1:8000/items/?skip=0&limit=10
```

-   `?` starts query parameter list
-   `&` separates query parameters

### Default Query Parameters

```python
@app.get("/items/")
def read_items(q: str = None):
    return {"q": q}
```

-   `q = None` default value

### Required Query Parameters

```python
@app.get("/items/")
def read_items(q: str):
    return {"q": q}
```

-   `q` is required

### Optional Query Parameters

```python
@app.get("/items/")
def read_items(q: str | None = None):
    return {"q": q}
```

-   `q = None` is optional and default `None`

## Multiple Path and Query Parameters

!!! info

    FasAPI detects all path parameters and query parameters by name.

```python
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False):
    ...
    return item
```

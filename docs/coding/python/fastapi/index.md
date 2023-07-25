# Python FastAPI :simple-fastapi:

FastAPI[^1] is a modern, fast (high-performance), web framework for building APIs.

!!! info

    FastAPI takes advantage of Python type hints.

**Features**

Fast, high performance, fast to code, intuitive, short, robust, standards-based

## Installation

```terminal
pip install fastapi
```

!!! info

    ASGI server ist needed for production:

    -  [Uvicorn](https://www.uvicorn.org/)
    -  [Hypercorn](https://pgjones.gitlab.io/hypercorn/)

    ```terminal
    pip install "uvicorn[standard]"
    ```

[^1]: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

## Interactive API Docs (automatic)

| **Swagger UI**[^2]                                       | **ReDoc**[^3]                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------- |
| [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) | [http://127.0.0.1:8000/redoc](http://http://127.0.0.1:8000/redoc) |

## HTTP Methods

!!! note

    FastAPI works with the OpenAPI Schema.

| HTTP Method | Description | FastAPI Decorator |
| ----------- | ----------- | ----------------- |
| GET         | Read data   | `@app.get()`      |
| POST        | Create data | `@app.post()`     |
| PUT         | Update data | `@app.put()`      |
| DELETE      | Delete data | `@app.delete()`   |

Methods in FastAPI are defined with the `@app.<method>()` decorator.

```python
@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

## Example

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

```terminal
uvicorn main:app --reload
```

[^1]: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
[^2]: [https://swagger.io/tools/swagger-ui/](https://swagger.io/tools/swagger-ui/)
[^3]: [https://github.com/Redocly/redoc](https://github.com/Redocly/redoc)

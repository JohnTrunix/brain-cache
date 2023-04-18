# Fast API Request Body

!!! info

    Sending data to server/client, the data is sent in the request body.

    - API almost has to send response body.
    - Client don't have to send often request body.

## Datamodel Creation

!!! note

    Datamodels are created with `pydantic` library.

    Same logic with `optional, default, required` parameters.

=== "Backend gets POST request"

    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        description: str | None = None
        price: float
        tax: float | None = None

    app = FastAPI()

    @app.post("/items/")
    async def create_item(item: Item):
        return item
    ```

=== "Result"

    ```json title="Response"
    {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    },
    {
        "name": "Foo",
        "price": 45.2
    }
    ```

## Data Model Usage

!!! tip

    `Item` Datamodel dict can be updated with new key-value pairs.

```python hl_lines="11 12 13 14"
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```

### Request Body & Path & Query Parameters

!!! info

    FasAPI detects/defines all parameters name, also in Datamodels.

```python hl_lines="9 10"
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

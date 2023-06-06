# Internet Standards & Encodings

## URL Encoding

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

## Date & Time Formats

| Name            | Format                            | Example                         |
| --------------- | --------------------------------- | ------------------------------- |
| UNIX Time       | `int`                             | 1571081990                      |
| ISO 8601        | `YYYY-MM-DD hh:mm:ss.ss`          | 2019-10-14T12:33:10+00:00       |
| RFC 3339        | `YYYY-MM-DDThh:mm:ss.sssZ`        | 2019-10-14T12:33:10.000Z        |
| RFC (2)822/5322 | `ddd, DD MMM YYYY hh:mm:ss +zzzz` | Mon, 14 Oct 2019 12:33:10 +0000 |
| RFC 7231        | `ddd, DD MMM YYYY hh:mm:ss GMT`   | Mon, 14 Oct 2019 12:33:10 GMT   |

## HTTP & URI

### URI Formats

| Name                    | Example                                                               |
| ----------------------- | --------------------------------------------------------------------- |
| URI / URL               | `https://www.example.com:8080/path/to/resource?query=string#fragment` |
| IRI / IRL               | `http://localhost/api/products/تلفاز`                                 |
| URI Template (RFC 6570) | `https://www.example.com/{version}/path/to/{resource}`                |
| Ressource Formats       | `html`, `json`, `yaml`, `xml`, `binary`, `text`                       |

### HTTP Methods

| Name   | Description                                            |
| ------ | ------------------------------------------------------ |
| GET    | Requests a representation of the specified resource    |
| POST   | Submits data to be processed to the specified resource |
| PUT    | Uploads a representation of the specified resource     |
| DELETE | Deletes the specified resource                         |

### HTTP Status Codes

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

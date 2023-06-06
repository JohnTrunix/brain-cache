# Requests

!!! info

    Requests is a Python library for HTTP requests. It is used to send HTTP requests to a server and receive a response. There is also an inbuilt library called `urllib` for the same purpose but a little bit more complicated to use.

## Get Request

=== "requests"

    ```python
    import requests

    response = requests.get("https://example.com")
    print(response.status_code)
    print(response.text)

    # Output:
    # >>> 200
    # >>> <!doctype html>
    # >>> <html>
    # >>> <head>
    # >>> <title>Example Domain</title>
    # >>> ...
    ```

=== "urllib"

    ```python
    import urllib.request

    response = urllib.request.urlopen("https://example.com")
    print(response.status)
    print(response.read().decode("utf-8"))

    # Output:
    # >>> 200
    # >>> <!doctype html>
    # >>> <html>
    # >>> <head>
    # >>> <title>Example Domain</title>
    # >>> ...
    ```

## Get & Save File

=== "requests"

    ```python
    import requests

    response = requests.get("https://example.com/example.csv")
    with open("example.csv", "wb") as file:
        file.write(response.content)
    ```

=== "urllib"

    ```python
    import urllib.request

    response = urllib.request.urlopen("https://example.com/example.csv")
    with open("example.csv", "wb") as file:
        file.write(response.read())
    ```

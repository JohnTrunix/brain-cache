# JavaScript Error Handling

```javascript
try {
    // code that may throw an error
    throw new Error("Error message"); // throw a custom error
} catch (err) {
    // code to handle the error
} finally {
    // code to be executed regardless of the error at the end
}
```

-   `try` - code that may throw an error
-   `catch` - code to handle the error
-   `finally` - code to that will be executed at the end of the `try` block
-   `throw new Error("Error message")` - throw a custom error

## Debugging

-   `console.log()` - print to the console
-   `debugger;` - stop execution and call debugging function

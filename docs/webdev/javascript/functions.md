# JavaScript Functions

```javascript
function add(a, b = 0) {
    let x = 1;
    return a + b;
}

let sum = add(1, 2); // sum = 3
```

-   `a` and `b` are parameters
-   `b = 0` defines a default parameter
-   `let x` is a local variable and is not accessible outside the function

!!! info

    - Function declaration is hoisted to the top of the scope.
    - Accessing `add` without `()` returns the function object and not the result
      ```javascript
        let sum = add
        let result = sum(1, 2) // result = 3
      ```

### Default Parameters

```javascript
function add(a = 0, b = 0) {
    return a + b;
}
```

### Rest Parameters

```javascript
function add(...numbers) {
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
}
```

### `this` in Functions

```javascript
const person = {
    name: "John",
    age: 30,
    greet: function () {
        console.log(`Hello, my name is ${this.name}`);
    },
};

person.greet(); // Hello, my name is John
```

-   `this` refers to the object that called the function
-   `bind`, `call` and `apply` can be used to change the `this` value

## Arrow Function

```javascript
let add = (a, b) => a + b;
let sum = add(1, 2); // sum = 3
```

## JS Default Functions

-   `alert()` - displays an alert box with a message and an OK button
-   `console.log()` - writes a message to the console
-   `eval()` - evaluates a string as a JavaScript expression
-   `isFinite()` - determines whether a number is finite
-   `isNaN()` - determines whether a value is NaN
-   `parseFloat()` - parses a string and returns a floating point number
-   `encodeURI()` - encodes a URI
-   `decodeURI()` - decodes a URI
-   `setTimeout()` - calls a function after a specified number of milliseconds
-   `setInterval()` - calls a function repeatedly, after a specified number of
    milliseconds

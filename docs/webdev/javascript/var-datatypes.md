# JavaScript Variables & Datatypes

## Datatypes

```javascript
var x; // undefined
var x = 5; // number
var x = 3.14; // number
var x = "Test"; // string
var x = ["Test", "Test2"]; // array
var x = true; // boolean
var x = null; // null
```

### Objects

```javascript
// object
var object = {
    key1 "value1",
    key2: 12,
    total: function() {
        return this.key1 + this.key2;
    }
};

object.key1 = "new value"; // change value
object[key2]++; // increment key2
total = object.total(); // call function
```

## Variable Scopes

| type  | scope                 | redeclare           | update              | hoisting     | hoisting init   |
| ----- | --------------------- | ------------------- | ------------------- | ------------ | --------------- |
| var   | global/function/local | :octicons-check-16: | :octicons-check-16: | top of scope | `undefined`     |
| let   | block                 | :octicons-x-16:     | :octicons-check-16: | top of scope | :octicons-x-16: |
| const | block                 | :octicons-x-16:     | :octicons-x-16:     | top of scope | :octicons-x-16: |

### var

-   `var` can be redeclared and updated (global/function/local scoped)

```javascript
var x = 10; // var Variable

function test() {
    var y = 20;
    var x = y;
    console.log(x); // 20
}
```

### let

-   `let` can't be redeclared but updated (block scoped)

```javascript
let x = 10; // let Variable

let x = 20; // error can't redeclare
x = 20; // update

function test() {
    let x = 20; // no error because function scoped
}
```

### const

-   `const` can't be redeclared or updated (block scoped)

```javascript
const x = 10; // const Variable

const x = 20; // error can't redeclare
x = 20; // error can't update

function test() {
    const x = 20; // no error because function scoped
}
```

-   Objects and Arrays can be updated

```javascript
const object = {
    key1: "value1",
    key2: 12,
};

object.key1 = "new value"; // no error
```

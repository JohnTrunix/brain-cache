# JavaScript Operators & Conditionals

## if-Condition

```javascript
if (condition) {
    // code
} else if (condition) {
    // code
} else {
    // code
}
```

## switch-Condition

```javascript
switch (expression) {
    case "value1":
        // code
        break;
    case "value2"
    case "value3":
        // code
        break;
    default:
    // code
}
```

## Logical Operators

| operator | description | example `var x = 5; var y = 10` |
| -------- | ----------- | ------------------------------- |
| &&       | and         | `x < 10 && y > 9 -> true`       |
| \|\|     | or          | `x < 10` \|\| `y > 15 -> true`  |
| !        | not         | `!(x == y) -> true`             |

## Boolean Operators

| operator | description                        | example `var x = 5;` |
| -------- | ---------------------------------- | -------------------- |
| ==       | equal (value)                      | `x == "5" -> true`   |
| ===      | strictly equal (value & type)      | `x === 5 -> true`    |
| !=       | not equal (value)                  | `x != 8 -> true`     |
| !==      | not strictly equal (value or type) | `x !== "5" -> true`  |
| >        | greater than                       | `x > 8 -> false`     |
| <        | less than                          | `x < 8 -> true`      |
| >=       | greater than or equal              | `x >= 8 -> false`    |
| <=       | less than or equal                 | `x <= 5 -> true`     |

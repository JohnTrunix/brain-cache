# JavaScript Loops & Iteration

## for-Loop

```javascript
for (var i = 0; i < 10; i++) {
    // code
}
```

## for in Loop

```javascript
var object = {
    key1: "value1",
    key2: 12,
};

for (var key in object) {
    console.log(key + ": " + object[key]);
}
```

## while-Loop

```javascript
var i = 0;
while (i < 10) {
    // code
    i++;
}
```

## do while-Loop

```javascript
var i = 0;
do {
    // code
    i++;
} while (i < 10);
```

!!! info "Difference between while and do while"

    The `do while` loop will always execute at least once, even if the condition is false.

## Break & Continue

```javascript
for (var i = 0; i < 10; i++) {
    if (i == 5) {
        break; // stop & exit loop
    }
    if (i == 3) {
        continue; // skip rest of iteration
    }
    // code
}
```

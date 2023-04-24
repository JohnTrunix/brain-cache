# JavaScript Classes

=== "Declaration"

    ```javascript
    class Rectangle {
        constructor(height, width) {
            this.height = height;
            this.width = width;
            this.area = this.calcArea();
        }
        get area() {
            return this.calcArea();
        }
        calcArea() {
            return this.height * this.width;
        }
    }
    ```

=== "Anonymous Class"

    ```javascript hl_lines="1"
    const Rectangle = class {
        constructor(height, width) {
            this.height = height;
            this.width = width;
            this.area = this.calcArea();
        }
        get area() {
            return this.calcArea();
        }
        calcArea() {
            return this.height * this.width;
        }
    };
    ```

=== "Expression"

    ```javascript hl_lines="1"
    const Rectangle = class Rectangle {
        constructor(height, width) {
            this.height = height;
            this.width = width;
            this.area = this.calcArea();
        }
        get area() {
            return this.calcArea();
        }
        calcArea() {
            return this.height * this.width;
        }
    };
    ```

## Instance

```javascript
const rect = new Rectangle(10, 20);
console.log(rect.area); // 200
```

## General Class Structure

```javascript
class ClassName {
    instanceField;
    static staticField;
    #privateField;
    static #privateStaticField;

    constructor(value) {
        this.property = value;
        this.#privateProperty = value;
    }
    get property() {
        return this.property;
    }
    set property(value) {
        this.property = value;
    }
    method(parameter) {
        // code with this.* and parameter
    }
    static method(parameter) {
        // code withouth this.*
    }
    #privateMethod() {
        // code with this.* and parameter
    }
}
```

-   `instanceField` is a field accessible from all instances of the class
-   `constructor()` method which builds the class instance
-   `get` and `set` methods for properties (accessors)
-   `static` methods and fields are only accessible from the class itself `ClassName.method()`

## Class Inheritance

```javascript
class A {
    constructor(value) {
        this.a = value;
    }
    methodA() {
        console.log("A");
    }
}

class B extends A {
    constructor(value1, value2) {
        super(value1);
        this.b = value2;
    }
    methodB() {
        console.log("B");
    }
}
```

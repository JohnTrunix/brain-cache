# Java

```java
/*
Multiline comment
*/

// single line comment
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

## Variables

**Primitive types**:

-   `String` - characters
-   `char` - single character
-   `int` - integer
-   `float` - floating point number
-   `boolean` - true or false

```java
// declaration
type variableName = value;

// other possible declarations
type variableName;
variableName = value;

int anInteger = 1;

// multiple declarations
type x, y, z;
x = y = z = value;

int x = 1, y = 2, z = 3;
```

**Keywords**:

-   `final` - constant
-   `static` - class variable
-   `public` - accessible from anywhere
-   `private` - accessible only from the class
-   `protected` - accessible from the class and subclasses
-   `void` - no return value

```java
final type variableName = value;

final int CONSTANT = 1;
```

## Data Types

-   `byte` - 1byte numbers: -128 to 127
-   `short` - 2bytes numbers: -32,768 to 32,767

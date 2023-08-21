# Functions

Functions are building blocks of a program. They can take zero or more arguments and return zero or more values.

## Simple Function

```go
//  [...]

func add(x int, y int) int { // x, y are parameters, int is the return type
	return x + y
}

func main() {
	result := add(1, 2)
	fmt.Println(result) // 3
}
```

## Multiple Return Values

A function can return multiple values. The return values are separated by commas.

```go
//  [...]

func swap(x int, y int) (int, int) { // x, y are parameters, int is the return type
	return y, x
}

func main() {
	a, b := 1, 2
	fmt.Println(a, b) // 1 2
	a, b = swap(a, b)
	fmt.Println(a, b) // 2 1
}
```

## Variadic Functions

Variadic functions are functions which can be called with a variable number of arguments. The type of the last parameter is prefixed with an ellipsis (...). The function can be called with any number of arguments for that parameter including zero.

```go
//  [...]

func sum(nums ...int) int { // nums is a variadic parameter
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}

func main() {
    fmt.Println(sum(1, 2, 3)) // 6
    fmt.Println(sum(1, 2, 3, 4, 5)) // 15
    fmt.Println(sum()) // 0
}
```

## Anonymous Functions (Closures)

Closures are anonymous functions which can be assigned to a variable.

```go
//  [...]

func adder() func(int) int {
    sum := 0
    return func(x int) int { // returns an anonymous function
        sum += x
        return sum
    }
}

func main() {
    sum := adder()
    for i := 0; i < 10; i++ {
        fmt.Println(sum(i))
    }
}
```

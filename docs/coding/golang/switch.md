# Switch

A `switch` statement is a shorter way to write a sequence of `if - else` statements. It runs the first case whose value is equal to the condition expression.

```go
// [...]

func main() {
    x := 10
    switch x {
    case 5:
        fmt.Println("x is equal to 5")
    case 10:
        fmt.Println("x is equal to 10")
    default:
        fmt.Println("x is not equal to 5 or 10")
    }
}
```

**Note:**

-   the `default` case is optional and it is executed if no other case matches.
-   the evaluation order is from top to bottom, stopping when a case succeeds.

## Switch without a condition

Switch without a condition is the same as `switch true`.

```go
// [...]

func main(){
    x := 10
    switch {
    case x > 5:
        fmt.Println("x is greater than 5")
    case x < 5:
        fmt.Println("x is less than 5")
    default:
        fmt.Println("x is equal to 5")
    }
}
```

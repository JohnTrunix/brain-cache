# If Conditionals

## If

```go
// [...]

func main() {
    x := 10
    if x > 5 {
        fmt.Println("x is greater than 5")
    }
}
```

## If with a short statement

```go
// [...]

func main() {
    x := 10
    if x /= 2; x > 5 {
        fmt.Println("x is greater than 5")
    }
}
```

**Note:** here the short statement `x /= 2` is used to divide `x` by 2 and assign the result to `x`.

## If, else if, else

```go
// [...]

func main() {
    x := 5
    if x > 5 {
        fmt.Println("x is greater than 5")
    } else if x < 5{
        fmt.Println("x is less than 5")
    } else {
        fmt.Println("x is equal to 5")
    }
}
```

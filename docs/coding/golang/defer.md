# Defer

`defer` is used to ensure that a function call is performed later in a programs execution, no matter the function exits normally or panics.

```go
// [...]

func main() {
    defer fmt.Println("world")
    fmt.Println("hello")
}
```

```
hello
world
```

Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed in last-in-first-out order.

```go
// [...]

func main() {
    for i := 0; i < 10; i++ {
        defer fmt.Println(i)
    }
    fmt.Println("done")
}
```

```
done
9
8
7
...
```

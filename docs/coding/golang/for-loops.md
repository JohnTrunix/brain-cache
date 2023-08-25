# For Loops

In Go, there is only one looping construct, the `for` loop. The basic `for` loop has three components separated by semicolons:

-   the init statement: executed before the first iteration
-   the condition expression: evaluated before every iteration
-   the post statement: executed at the end of every iteration

```go
// [...]

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
		fmt.Println(sum)
	}
}
```

## For continued

The init and post statements are optional.

```go
// [...]

func main() {
    sum := 1
    for ; sum < 1000; {
        sum += sum
    }
    fmt.Println(sum)
}
```

## While replacement

At that point you can drop the semicolons: C's `while` is spelled `for` in Go.

```go
// [...]

func main() {
    sum := 1
    for sum < 1000 {
        sum += sum
    }
    fmt.Println(sum)
}
```

## Infinite loop

If you omit the loop condition it loops forever, so an infinite loop is compactly expressed.

```go
// [...]

func main() {
    for {
        // do something infinitely many times
    }
}
```

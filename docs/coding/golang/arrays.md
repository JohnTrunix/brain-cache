# Arrays and Slices

!!! note

    Arrays have per default fix defined lengths.

## Assign by Position

```go
// [...]

func main() {
	// assign by position
	var a [2]int
	a[0] = 10
	a[1] = 20
	a[0] = a[0] + a[1]
	fmt.Println(a)
}
```

## Assign by Declaration

```go
// [...]

func main() {

	// assign directly
	b := [2]int{10, 20}
	fmt.Println(b)
}
```

## Slicing

Slicing is a way to create a new array from an existing array. Start index is inclusive and end index is exclusive. The syntax is `array[start:end]`.

```go
// [...]

func main() {
	numbers := [8]int{1, 2, 3, 4, 5, 6, 7, 8}

	var slice []int = numbers[0:4] // slice from 0 to 4 (exclusive -> 4-1 = 3)
	fmt.Println(slice)
}
```

## Dynamically-sized Arrays

Arrays can be dynamically sized by using the `make` function. With the `append` function, you can add elements to the array. Removing elements is not directly possible, but you can create a new array without the element you want to remove (with slicing).

```go
// [...]

func main() {
	dynamic := make([]int, 5)
	fmt.Println(dynamic)

	dynamic = append(dynamic, 10, 20)
	fmt.Println(dynamic)
}
```

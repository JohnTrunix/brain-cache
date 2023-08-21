# Structs

Structs are user-defined types that can be used to store a collection of fileds into a single unit. They are similar to classes in object-oriented languages.

## Basic Structs

```go
// [...]

type Rectangle struct {
	Width  int
	Height int
}

type Circle struct {
	Radius int
}

func main() {
	r := Rectangle{
		Width:  10,
		Height: 4,
	}
	c := Circle{
		Radius: 12,
	}
}
```

## Advanced Structs

You can also embed structs into other structs. This is similar to inheritance in object-oriented languages.

```go
// [...]

type Shape struct {
	Edges int
}

type Rectangle struct {
	Width  int
	Height int
	Shape
}

type Circle struct {
	Radius int
	Shape
}

func main() {
	r := Rectangle{
		Width:  10,
		Height: 4,
		Shape: Shape{
			Edges: 4,
		},
	}
	c := Circle{
		Radius: 12,
		Shape: Shape{
			Edges: 0,
		},
	}
}
```

# Interfaces

Interfaces are a way to define a set of methods that a type must implement. This allows you to define a function that can take any type that implements the interface. This is similar to duck typing in Python. Interfaces are defined as a set of method signatures.

```go
// [...]

// Area Interface
type Area interface {
	Area() float64
}

// Different Structs
type Rectangle struct {
	Width  float64
	Height float64
}

type Circle struct {
	Radius float64
}

// Add Area() function to structs
func (c Circle) Area() float64 {
	return 3.14 * math.Pow(c.Radius, 2)
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

// main calc function
func calcArea(obj Area) float64 {
	return obj.Area()
}

func main() {
	r := Rectangle{
		Width:  10,
		Height: 4,
	}
	c := Circle{
		Radius: 12,
	}
	rArea := calcArea(r)
	cArea := calcArea(c)
}
```

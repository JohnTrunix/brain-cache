# Pointers

Pointers are used to store the memory address of another variable. They are used to pass large data structures to functions without copying them. They are also used to create linked lists and other data structures. With pointers, you can read, write, modify and delete the value of the variable they point to.

```go
// [...]

func main() {
	x := 100

	pX := &x         // pointer to x
	fmt.Println(*pX) // read value with pointer

	*pX = 20         // set new value with pointer
	fmt.Println(*pX) // read value with pointer

	*pX = *pX / 2    // divide
	fmt.Println(*pX) // read value with pointer
}
```

## Pointers to struct

```go
// [...]

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v

	p.X = 1e2
	p.Y = p.Y - 20
	fmt.Println(v)
}
```

## Usecase (link to nodes)

```go
package main

import "fmt"

type Node struct {
	Data int
	Next *Node
}

func main() {

	node3 := &Node{Data: 30, Next: nil}
	node2 := &Node{Data: 20, Next: node3}
	node1 := &Node{Data: 10, Next: node2}

	current := node1
	for current != nil {
		fmt.Println(current.Data)
		current = current.Next
	}
}
```

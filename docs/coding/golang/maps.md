# Maps

Maps are Go's built-in associative data type (sometimes called hashes or dicts in other languages). Maps are unordered collections of key-value pairs. Maps are declared using the `map` keyword, followed by the key and value types in square brackets. The key type must be comparable (i.e. it must support the `==` operator). The value type can be any type.

```go
// [...]

func main() {
	m := make(map[string]int) // create empty map
	m["key1"] = 10            // set value
	m["key2"] = 20            // set value
	fmt.Println(m)            // map[key1:10 key2:20]

	m["key1"] = 30 // update value
	fmt.Println(m) // map[key1:30 key2:20]

	delete(m, "key1") // delete key
	fmt.Println(m)   // map[key2:20]

	v, ok := m["key1"] // check if key exists
	fmt.Println(v, ok) // 0 false

	val2 := m["key2"] // get value
	fmt.Println(val2) // 20
}
```

# Go Datatypes

!!! info

    Every not declared `variable` is 0 by default!

## Literals

!!! note

    Literals can have differenct Base, like `0x` for Hexadecimal, `0b` for Binary, `0o` for Octal, etc.

| Type    | Example                                              |
| ------- | ---------------------------------------------------- |
| Integer | `14`, `0b`, `0o` (decimal, binary, octal)            |
| Float   | `3.14`, `1.6e-10`                                    |
| Rune    | `a`, `\141`, `\u0061`, `\U00000061`, `\n`, `\t`, `\` |

**Bitshifting**

```go
1 << 10 // 1024
10 >> 1 // 5
```

### Integer Numeric Types

!!! note

    For general purpose use `int`

| Type   | min                  | max                  | size   |
| ------ | -------------------- | -------------------- | ------ |
| int8   | -128                 | 127                  | 8 bit  |
| int16  | -32768               | 32767                | 16 bit |
| int32  | -2147483648          | 2147483647           | 32 bit |
| int64  | -9223372036854775808 | 9223372036854775807  | 64 bit |
| uint8  | 0                    | 255                  | 8 bit  |
| uint16 | 0                    | 65535                | 16 bit |
| uint32 | 0                    | 4294967295           | 32 bit |
| uint64 | 0                    | 18446744073709551615 | 64 bit |

```go
var a int = 14
var b int8 = 14
var c uint8 = 14
```

### Floating Point Numeric Types

| Type    | min      | max      | size   |
| ------- | -------- | -------- | ------ |
| float32 | 1.2E-38  | 3.4E+38  | 32 bit |
| float64 | 2.2E-308 | 1.7E+308 | 64 bit |

```go
var a float = 3.14
var b float32 = 3.14
var c float64 = 3.14
```

## Boolean

```go
var b bool
b = true
b = false
```

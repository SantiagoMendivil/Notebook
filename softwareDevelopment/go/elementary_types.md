# Table of contents
- [Table of contents](#table-of-contents)
- [Elementary Types](#elementary-types)
  - [Boolean Type](#boolean-type)
  - [Numerical Type](#numerical-type)
    - [Integers and Floating-point Numbers](#integers-and-floating-point-numbers)
- [Format Specifiers](#format-specifiers)
- [Random Numbers](#random-numbers)
- [Character Type](#character-type)
- [The unicode package](#the-unicode-package)

# Elementary Types
The three main elementary types in Go are: Boolean, Numeric, character. 

## Boolean Type 
The possible values are **true** or **false**

## Numerical Type 
### Integers and Floating-point Numbers 

- int8 (-128 to 127)
- int16 (-32768 to 32767)
- int32 (− 2,147,483,648 to 2,147,483,647)
- int64 (− 9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)

For unsigned integers: 

- uint8 (with the alias byte, 0 to 255)
- uint16 (0 to 65,535)
- uint32 (0 to 4,294,967,295)
- uint64 (0 to 18,446,744,073,709,551,615)


For floats 

- float32 (± 1O−451O−45 to ± 3.4∗1O383.4∗1O38 )
- float64 (± 5∗1O−3245∗1O−324 to 1.7∗1O3081.7∗1O308 )

# Format Specifiers
Formatting strings with these kind of values can be confusing at some point, but let's review each of the possibilties when working with integer or floating variables. 

- %d: Is used as a format specifier for integers (%x or %X can be used for a hexadecimal representation)
- %g: is used for float types (%f gives a floating-point, and %e gives a scientific notation). 
- %0nd shows an integer with n digits, and leading 0 is necessary 
- %n.mg represents the number with a precision of m digits and width of n digits. 

# Random Numbers 
```go 
import "math/rand"

func main () {
    a := rand.Int() // Generates a random number 
    b := rand.Intn(8) // Generates a random number in [0, n]
}
```


# Character Type 
The characters are a special case of integers. The byte type is an alias for uint8, and this is okay for traditional ASCII-encoding for characters (1 byte). A byte type variable is declared as: 

```go 
var ch byte = 'A'
```

or 

```go 
var ch byte = 65
```

or

```go 
var ch byte = '\x41'
```


# The unicode package 
The package unicode has some useful functions for testing characters. 
- Testing for a letter: `unicode.IsLetter(ch)`
- Testing for a digit: `unicode.IsDigit(ch)`
- Testing for a whiteSpace character: `unicode.IsSpace(ch)`
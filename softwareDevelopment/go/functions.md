# Table of contents
- [Table of contents](#table-of-contents)
- [Functions](#functions)
  - [Function declarations](#function-declarations)
    - [Simple function](#simple-function)
    - [Function returning an object](#function-returning-an-object)
    - [Returning multiple objects](#returning-multiple-objects)

# Functions
The simplest function declaration has the format: 

```go 
func functionName () {

}
```

Between the parenthesis, goes the parameters. The main function as a starting point is required with no arguments and no return type. 
```go 
package main 
import "fmt"

func main () {

}
```

## Function declarations 
----------
### Simple function 
```go 
func func_name(param1 type1, param2 type2, ...) {
    ...
}
```

### Function returning an object 
```go 
func func_name(param1 type1, param2 type2, ...) type1 {
    ...
}
```

or 

```go 
func func_name(param1 type1, param2 type2, ...) ret1 type1 {
    ...
}
```
Where ret1 is a variable of type `type1` to be returned.

### Returning multiple objects
```go 
func func_name(param1 type1, param2 type2, ...) (ret1 type1, ret2 type2, ...) {

}
```

A smaller function can be written as the following: 
```go 
func Sum(a, b int) int { return a + b }
```



# Table of contents
- [Table of contents](#table-of-contents)
- [Import Functionality](#import-functionality)
  - [Packages](#packages)
  - [Import keyword](#import-keyword)
- [Variable Types](#variable-types)
  - [Types and Examples](#types-and-examples)
  - [Aliases for Types](#aliases-for-types)
  - [constants](#constants)

# Import Functionality 
## Packages
A library, module, or namespace in any other language is called a package. Packages are a way to structure code. A program is constructed as a package which may use facilities from other packages. A package is often abbreviated as 'pkg'. 

The package to which the code-file belongs must be indicated on the first line. A package name is written in **lowercase** letters. 

```go 
package main
```

A standalone executable belongs to *main*. Each Go application contains one main. 

## Import keyword 
```go 
package main 
import "fmt"
```

The import line tells Go that this program needs functions, or other elements from the package fmt. 

There are several ways on how to import a module in our go files. 
1. In single lines 
```go 
import "fmt"
import "os"
```
2. In one line 
```go 
import "fmt"; import "os"
```
3. Between parentheses 
```go 
import (
    "fmt"
    "os"
)
```
4. With alias 
```go 
import fm "fmt"
```

# Variable Types 
Variables contain data, and data can be of different data types. Go is a statically typed language. It means the compiler must know the types of all the variables, either because they were explicitly indicated, or because the compiler can infer the type from the code context. 

## Types and Examples 
- elementary (or primivite): int, float, bool, string 
- structured (or composite): struct, array, slice, map, channel 
- interfaces: They describe the behavior of a type. 

A structured type, which has no real value(yet), has the value **nil** which is also the default value for these types. 

```go 
var var1 type1
```

## Aliases for Types 
```go 
type IZ int 
```
Now to declare an integer variable we have to use the alias: 
```go 
var a IZ = 5
```

You can also set various types in one line: 
```go 
type (
  IZ int 
  FZ float32 
  STR string 
)
```
## constants 

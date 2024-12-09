package main

import (
	"fmt" // Package implementing formatted I/O.
)

func PrintMessage(message string) {
	fmt.Println(message)
}

func PrintTypes() {
	var identiier int = 1 // Declares a variable of type int.
	var decision bool = true
	name := "Santiago Mendivil" // Ignores the type and assigns the value

	// The operator := can't be used outside a function.

	// For printing it follows the same nature as in a C-like program.
	// %T is used to print the type of the variable.
	// %v is used to print the value of the variable.
	// %d specifies format for decimal integer.
	// %s specifies format for string.

	fmt.Printf("Type: %T\n", identiier)
	fmt.Printf("Type: %T\n", decision)
	fmt.Printf("Type: %T\n", name)
}

func main() {
	fmt.Println("Hello, World!")

	PrintMessage("What am I doing here? 😭")
	PrintTypes()
}

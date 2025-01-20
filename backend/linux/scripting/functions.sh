#!/usr/bin/bash

# Functions in bash scripting
# ########################################################
# Functions are used to group commands together
# Functions are defined using the following syntax:
# function_name() {
#     command1
#     command2
#     command3
# }
# The function is called using the function_name syntax
# Functions can take arguments
# Arguments are accessed using the $1, $2, $3, etc. syntax
# The return value of a function is the exit status of the last command
# The return statement is used to return a value from a function

# ########################################################

# Simple function
function hello() {
    echo "Hello, World!"
}

hello # Calling the function 


# Function with arguments
function greet() {
    echo "Hello, $1!"
}

greet "Alice" # Calling the function with an argument


# Function with return value (integer)
function add() {
    return $(($1 + $2))
}

add 5 3 # Calling the function with arguments


# Function with return value (string)
function concat() {
    echo "$1$2"
}

result=$(concat "Hello, " "World!") # Calling the function with arguments


# Function with local variables
function local_var() {
    local name="Alice"
    echo "Hello, $name!"
}

local_var # Calling the function

#!/usr/bin/bash

# Numbers in bash scripting

# ########################################################
# Numbers in bash scripting are treated as strings
# We can perform arithmetic operations using the $(( )) syntax

echo $(( 10 + 20 ))

x=10
y=5

# These two methods return the same result and works the same
echo $(( x + y )) 
echo $(expr $x + $y)
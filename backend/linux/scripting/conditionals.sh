#!/usr/bin/bash 

# Conditionals im Bash Scripting
# ########################################################
# There are two ways of using conditionals in bash scripting
#   1. Using the [ ] syntax 
#   2. Using the [[ ]] syntax
#   3. Using the (( )) syntax

# The [ ] 
#   - Evaluates basic expressions 
#   - Synonymous with the test command
#   - Works with expressions like comparing strings, integers, files, etc
# The [[ ]] 
#   - Allows complex expressions that use && or || operators
#   - Works with regular expressions (=~)
# The (( ))
#   - Used for arithmetic operations
#   - Works with operators like +, -, *, /, etc
#   - Returns 0 if the expression is true and 1 if it is false

# ########################################################
# We can use the following operators to compare values in bash scripting 
# -eq: equal
# -ne: not equal
# -gt: greater than
# -lt: less than
# -ge: greater or equal
# -le: less or equal

# Variable to use 
read -p "Enter your age: " age

# Simple conditional 
if [ $age ]; then 
    echo "You are $age years old"
fi

# Conditional with an else statement
if [ $age -ge 18 ]; then 
    echo "You are an adult"
else 
    echo "You are a minor"
fi

# Conditional with an else if statement
if [ $age -ge 18 ]; then 
    echo "You are an adult"
elif [ $age -ge 13 ]; then 
    echo "You are a teenager"
else 
    echo "You are a child"
fi

# ########################################################
# Conditionals with operator 


# Conditional with multiple conditions using multiple [] and the [[ ]] syntax
if [ $age -ge 18 ] && [ $age -lt 65 ]; then 
    echo "You are an adult"
fi

if [[ $age -ge 18 && $age -lt 65 ]]; then 
    echo "You are an adult"
fi

# Conditional with multiple conditions using the -a flag
if [ $age -ge 18 -a $age -lt 65 ]; then 
    echo "You are an adult"
fi

# Conditional with multiple conditions using the -o flag
if [ $age -lt 18 -o $age -ge 65 ]; then 
    echo "You are not an adult"
fi
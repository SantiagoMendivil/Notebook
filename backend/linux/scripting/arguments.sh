#!/usr/bin/bash 

# Arguments in bash scripting
# ########################################################
# The arguments are received in the form of $1, $2, $3, etc
# it depends on the order that they are specified when calling the script

# We can read n number of arguments using the $@ variable
echo "All arguments: $@"

# We can count the number of arguments using the $# variable
echo "Number of arguments: $#"
# ########################################################
# Example 
args=("$@")

echo "Result: ${args[0]} ${args[1]} ${args[2]}"

for i in $@; do 
    echo "Argument: $i"
done

# ########################################################
# Read files from input arguments

while read line; do 
    echo "Line: $line"
done < $1
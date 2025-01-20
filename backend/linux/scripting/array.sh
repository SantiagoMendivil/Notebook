#!/usr/bin/bash

# Arrays in bash scripting
# ########################################################

# Arrays in bash scripting are used to store multiple values in a single variable
# The values are stored in a sequential manner
# The values are accessed using the index of the array
# The index of the array starts from 0

names=( "Alice" "Bob" "Charlie" "David" )
echo ${names[0]} # Prints Alice
echo ${names[1]} # Prints Bob
echo ${names[2]} # Prints Charlie
echo ${names[3]} # Prints David 

echo "Names are: ${names[*]}"

for i in ${names[@]}; do 
    echo "Name: $i"
done

# Get the last item 
echo "Last item: ${names[-1]}"

# Delete an item from the array
unset names[1] # Deletes Bob

# Add an item to the array
names[3]="Eve"

# Add an item to the end of the array
names+=( "Frank" )

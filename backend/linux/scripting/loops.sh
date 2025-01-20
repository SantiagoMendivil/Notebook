#!/usr/bin/bash 

# Loops in bash scripting
# ########################################################
# There are four types of loops in bash scripting 
#   1. For loop
#   2. While loop
#   3. Until loop
#   4. Select loop

# ########################################################
# While Loop 
number=1

while [ $number -le 10 ]; do 
    echo "Number: $number"
    number=$(( number + 1 ))
done
# ########################################################

# Until Loop 
num=1

until [ $num -ge 10 ]; do 
    echo "Number: $num"
    num=$(( num + 1 ))
done

# ########################################################
# For Loop
for i in {1..10}; do 
    echo "Number: $i"
done

# For with more information as in C
for (( i=1; i<=10; i++ )); do 
    echo "Number: $i"
done

# For loop with different step
for i in {1..10..2}; do 
    echo "Number: $i"
done

# For Loop with a range
for i in $(seq 1 10); do 
    echo "Number: $i"
done

# For Loop with an array
names=("Alice" "Bob" "Charlie")

for name in ${names[@]}; do 
    echo "Name: $name"
done

# ########################################################
# Select Loop
PS3="Select a name: "

select name in ${names[@]}; do # Syntax to select items from an array
    echo "You selected $name"
    break
done
# ########################################################
#!/usr/bin/bash 

# In this script we will see how to read inputs in different ways

# ########################################################
# Basic syntax to read an input 
read age
echo "You are $age years old"

# Read multiple values in a single line
echo "Enter your first name and last name"
read firstName lastName

# Read an input without asigning it to a variable
echo "Enter your city" 
read 
echo "Your city: $REPLY"

# You can show a message before reading an input with the -p flag
read -p "Enter your zip code: " zipCode

# You can hide the input with the -s flag
read -s -p "Enter your password: " password

# You can set a specific number of characters to read with the -n flag
read -n 3 -p "Enter the first three letters of your name: " letters

# You can set a timeout to read an input with the -t flag
read -t 10 -p "Enter your pin: " pin

# You can read an input from a file with the -r flag
read -r line < file.txt

# ########################################################
# Read multiple lines from a file
while read line; do 
    echo "Line: $line"
done < file.txt


# ########################################################
# Best practices 
# Always use the -p flag to show a message before reading an input
# Validate the user input 
read -p "Enter a number: " number
if [[ "$number" =~ ^[0-9]+$ ]]; then 
    echo "You entered a number"
else 
    echo "You did not enter a number"
fi
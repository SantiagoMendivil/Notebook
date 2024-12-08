#!/usr/bin/bash 

# In this script we will see how to print in the terminal
# and all the variants of the echo command

# ########################################################
# Basic echo commands 

# Prints a single message to the terminal 
echo "Hello World"


# Prints a variable's value to the terminal
name="John"
echo $name


# Prints multiple values to the terminal 
age=20
echo "Name: $name, Age: $age"


# We can interpret the escape characters in the string with -e flag
echo -e "\tTitle\n\tSubtitle"
echo -e "Name: $name, Age: $age\nNew Line"


# Avoid new lines with -n flag
echo -n "Loading"
echo "..."


# The output will be "Loading..."
# ########################################################
# Best practices and extra commands 

# Use printf instead of echo for better formatting
printf "Name: %s, Age: %d\n" $name $age

# Colors in the terminal 
echo -e "\e[31mRed Text\e[0m"
echo -e "\e[32mGreen Text\e[0m"
echo -e "\e[33mYellow Text\e[0m"
echo -e "\e[34mBlue Text\e[0m"
echo -e "\e[35mPurple Text\e[0m"
echo -e "\e[36mCyan Text\e[0m"
echo -e "\e[37mWhite Text\e[0m"

# Combine text and commands 
echo "Today is $(date)"

# Avoid unexpected characters with variables being printed 
echo "Hello ${name}!"


# ######################################################## 

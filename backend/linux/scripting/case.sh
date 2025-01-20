#!/usr/bin/bash

# Case statements in bash scripting
# ########################################################
# The case statement is used to match a value against a list of patterns
# The syntax is as follows:
# case $variable in
#     pattern1)
#         command1
#         command2
#         ;;
#     pattern2)
#         command1
#         command2
#         ;;
#     *)
#         command1
#         command2
#         ;;
# esac

# ########################################################
# Example 1: Basic case statement
read -p "Enter a number: " number

case $number in 
    1)
        echo "You entered one"
        ;;
    2)
        echo "You entered two"
        ;;
    3)
        echo "You entered three"
        ;;
    *)
        echo "You entered a number greater than three"
        ;;
esac
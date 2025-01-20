#!/usr/bin/bash

# Variables in bash scripting with declare 

# ########################################################
# Variables in bash scripting are defined using the following syntax
# variable_name=value

# The -r flag is used to declare a read-only variable
# The -i flag is used to declare an integer variable
# The -a flag is used to declare an array variable
# The -f flag is used to declare a function variable
# The -x flag is used to declare an environment variable
# The -p flag is used to display the attributes and values of a variable
declare -r pwdfile="/etc/passwd"

# This is the same as the above statement
readonly pswdfile="/etc/passwd"

# You can assign a default value if a variable is not defined 
echo ${username:-"No username set"}

# Special variable types 
# $0: The name of the script
# $1, $2, $3, etc: The arguments passed to the script
# $@: All the arguments passed to the script
# $#: The number of arguments passed to the script
# $?: The exit status of the last command
# $$: The process ID of the current script
# $USER: The username of the user running the script
# $HOSTNAME: The hostname of the machine running the script
# $SECONDS: The number of seconds the script has been running
# $RANDOM: Returns a random number
# $LINENO: Returns the current line number in the script
# $! : The process ID of the last background command
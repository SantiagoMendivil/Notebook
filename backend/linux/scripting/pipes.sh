#!/usr/bin/bash 

# Pipes in bash scripting
# ########################################################
# Pipes are used to redirect the output of one command to another command
# The syntax is as follows:
# command1 | command2
# The output of command1 is passed as input to command2
# The output of command1 is not saved to a file
# The output of command1 is not saved to a variable
# ########################################################

# Example 1: Basic pipe
ls -l | sort -k5 -rn
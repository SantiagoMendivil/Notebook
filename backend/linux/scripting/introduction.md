# Table of contents
- [Table of contents](#table-of-contents)
- [Introduction to Bash Scripting](#introduction-to-bash-scripting)
- [Creating an executable file](#creating-an-executable-file)
- [Basic structure](#basic-structure)
  - [Variables](#variables)
  - [Conditionals](#conditionals)
  - [Loops](#loops)
  - [Methods](#methods)
  - [Script debugging](#script-debugging)
  - [Script arguments](#script-arguments)
    - [Access the arguments](#access-the-arguments)
    - [Total number of arguments](#total-number-of-arguments)
    - [All the arguments](#all-the-arguments)
  - [Best Practices](#best-practices)
    - [Comments](#comments)
    - [Error handling](#error-handling)

# Introduction to Bash Scripting 
In this section I will explain about bash scripting and all the useful commands that we need to know in order to use the bash shell to execute specific programs. 

# Creating an executable file 
In order to make an executable file for bash scripting we can easily navigate into a directory, create a file with a .sh extension and give it some permissions in order to be executed by anyone that has access to it. 

```bash 
# Prints the working directory 
pwd

# Creates a directory that will contain all the scripts 
mkdir bash_scripting

# Navigates to the recently created directory 
cd bash_scripting

# Creates an executable file called helloworld.sh
touch helloworld.sh

# Prints specific information about the files 
ls -al 

# The output would look like this
# -rw-rw-r-- 1 user user dec 12 19:03 helloworld.sh

# Gives the file the permission to be executed 
chmod +x helloworld.sh

# Executes the file into the terminal
./helloworld.sh

# You can edit the contents of the file by using nano 
nano helloworld.sh
```

# Basic structure 
## Variables 
```bash 
NAME="your_name"
echo "Hello, $NAME"
```

## Conditionals 
```bash
if [[ -f file.txt ]]; then 
    echo "The file exists"
else 
    echo "The file doesn't exist"
fi 
```

## Loops 
```bash 
for i in {1..5}; do 
    echo "Number: $i"
done 
```

## Methods 
```bash 
my_function () {
    echo "Inside the function"
}

my_function
```

## Script debugging 
1. We have to execute the script in debugging mode to see each command before executing it. 
2. You can add messages for manual debugging inside the script 

```bash 
bash -x script.sh
```

## Script arguments 
You can pass arguments to the script in order to use them inside. 

### Access the arguments 
```bash 
echo "First argument: $1"
echo "Second argument: $2"
```

### Total number of arguments 
```bash 
echo "Total arguments: $#"
```

### All the arguments 
```bash 
echo "All the arguments: $@"
```

## Best Practices 
### Comments 
```bash 
# This is a comment in bash 
# This script will execute a sum 
read num1 
read num2 

sum=$(( num1 + num2 ))
echo $sum
```

### Error handling
Verify status errors with **set**
```bash 
set -e # Stops the script if any error occurs.
```
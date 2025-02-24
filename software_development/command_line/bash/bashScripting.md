# Table of contents 
- [Table of contents](#table-of-contents)

# Bash Scripting
## Configurate a script with bash
The script must have the extension of .sh. Then we must type a the top of the script

```bash
#!/bin/bash
```

Once we do this, we are ready to write bash code in the script.
In order to run this script in the bash terminal we just have to write the following line of code 

```bash
./file_name.extension
```

## Variables
As in other programming language, we need to write the name of the variable and then the value that this variable will contain. 
NOTE: Between the = sign and the value of the variable, there's no spaces 

```bash
variable=value
```

In order to access the value of this new variable we need to echo the name of the variable. 

```bash
echo $variable
```

## Conditionals
We use the if statements to control which set of commands within the script run. The structure of a conditional in bash. 

```bash
if [ $index -lt 5 ]
then
    echo $index
else 

    echo 5
fi 
```

We use the opeators for comparison, in bash they're:
- Equal: -eq
- Not equal: -ne
- Less than or equal: -le
- Less than: -lt
- Greater than or equal to: -ge
- Greater than: -gt
  
Is null: -z
Common operators for comparing strings are:
- Equal: ==
- Not equal: !=
For example, to compare the variables that contain a string:

```bash
if [ "$variable1" == "$variable2" ]
```

## Loops
For, while and until are used as loops to repeat a sequence of orders while a condition is met. 

```bash
For syntaxis:
for word in $paragraph
do
  echo $word
done
```
 
The variable word isn't declared until we use the for loop so that's why we don't use the $ sign at the top of the loop. But then, now that the variable word is define we now use the $ sign in order to access it.

```bash
While syntaxis:
while [ $index -lt 5 ]
do
  echo $index
  index=$((index + 1))
done
```

Note something here: The arithmetic in bash scripting uses the $((…)) syntax and within the brackets the variable name is not prepended with a $.


## Until syntaxis:
```bash
until [ $index -eq 5 ]
do
  echo $index
  index=$((index + 1))
done
```

This has the same structure as the while syntax


## Inputs
In order to have information from the user we use the read syntax. For example, if we want to read a number from the user and save it into a variable: 

```bash
echo "Guess a number"
read number
echo "You guessed $number"
```

Another way to access external data is to have the user add input arguments when they run the script.

saycolors red green blue

If we want to accept an indefinite number of arguments, you can iterate over them using the "$@" syntax. In order to modify the last line of saycolors we can use:

```bash
for color in "$@"
do
  echo $color
done
```

To access external files for our script we can assign the direction to a variable and specify a * at the end. And to iterate through the files in the variable we use: 

```bash
for file in files/*
do
  echo $file
done
```


## Aliases
We can set aliases for our bash scripts within our .bashrc or .bash_profile

```bash
alias saycolors='./saycolors.sh'
```

Or we can even add standard input arguments to our alias: 

```bash
alias saycolors='./saycolors.sh "green"'
```
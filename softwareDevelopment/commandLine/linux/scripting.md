# Table of contents
- [Table of contents](#table-of-contents)
- [Scripts With Linux](#scripts-with-linux)
  - [Print a message](#print-a-message)
  - [Read input](#read-input)
  - [Arithmetic Operations](#arithmetic-operations)
    - [expr](#expr)
  - [If Statement](#if-statement)
    - [Comparison Operators](#comparison-operators)
    - [OR and AND](#or-and-and)
    - [Multiple conditions](#multiple-conditions)
    - [If with simple calculation](#if-with-simple-calculation)

# Scripts With Linux

## Print a message 
```bash
echo "Message here"
```

## Read input 
We use the read keyword. Then the variable can be accessed by using the dollar sign. 

```bash 
read -p name 
echo "Welcome" $name
```

## Arithmetic Operations
### expr
For sums
```bash
#!/bin/bash 
a=5
b=10
sum=$(expr $a + $b)
echo "The sum is: $sum"
```

For substractions
```bash
#!/bin/bash 
a=5
b=10
res=$(expr $a + $b)
echo "The substraction is: $res"
```

For multiplications (We use the escape \ because the asterisk is a special bash keyword)
```bash
#!/bin/bash 
a=5
b=10
mul=$(expr $a \* $b)
echo "The sum is: $mul"
```


For division
```bash
#!/bin/bash 
a=5
b=10
quo=$(expr $a / $b)
echo "The quotient is: $quo"
```

## If Statement

### Comparison Operators 
-gt: Greater than 
-eq: equals to 
-lt: Less than 
-ge: Greater or equal than
-le: Less or equal than 
[]: Evaluate conditions


If it is a string: 
"": String
==: equals to 

```bash
read -p "Ingresa el valor de x: " x
read -p "Ingresa el valor de y: " y

if [ "$x" -gt "$y" ]; then
    echo "X is greater than Y"
elif [ "$x" -lt "$y" ]; then
    echo "X is less than Y"
elif [ "$x" -eq "$y" ]; then
    echo "X is equal to Y"
fi
```

### OR and AND
```bash
read -p "Write a character (y/n): " char

if [[ "$char" == "y" || "$char" == "Y" ]]; then
    echo "YES"
elif [[ "$char" == "n" || "$char" == "N" ]]; then
    echo "NO"
else
    echo "Invalid character"
fi
```

### Multiple conditions 
We can read inputs in several lines one by one by using -r after the `read` statement and before the variable name. 

Here is an example of multiple conditions on the logic for evaluating a triangle and its type: 

```bash
#!/bin/bash

# Read three integers, one per line
read -r a
read -r b
read -r c

# Check for triangle type
if [[ $a -eq $b && $b -eq $c ]]; then
    echo "EQUILATERAL"
elif [[ $a -eq $b || $b -eq $c || $a -eq $c ]]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
```


### If with simple calculation
```bash 
for num in $(seq 1 99); do
    if (( "$num % 2" != "0" )); then
        echo $num
    fi
done
```
Let's break down this code: 

- **for statement**: The for is initialized to be from 1 to 99 inclusive in a sequence using `seq`.
- **if**: The if is set to compare two expressions using double parenthesis and the expressions inside double quotes 
- **$num**: The variables allways are called with the dollar sign beside the variable's name.  
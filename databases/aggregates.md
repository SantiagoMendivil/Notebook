# Table of contents 
- [Table of contents](#table-of-contents)
- [Aggregate Functions](#aggregate-functions)
  - [COUNT](#count)
  - [SUM](#sum)
  - [MAX / MIN](#max--min)
  - [AVG](#avg)
  - [ROUND](#round)
  - [GROUP BY](#group-by)
  - [HAVING](#having)
  - [TIMESTAMP](#timestamp)

# Aggregate Functions 
## COUNT
Counts how many rows are in a table. 
- It takes the name of a column as an argument
- Counts the number of non-empty values in that column.

```sql
SELECT COUNT (*)
FROM table_name;
```

Here we want to count every row in a table so we pass * as an argument



## SUM
It sums the values in a row.
- It takes the name of a column as an argument 
- Returns the sum of all values in that column

```sql
SELECT SUM (downloads)
FROM fake_apps;
```


## MAX / MIN
It returns the maximum or minimum value from a table
- It takes a name of a column as an argument 
- It searches for the value that matches the aggregate function 
- It returns only the single value.

NOTE: If more than one value has the max or min value, it will return the value at the top.

```sql
SELECT MAX(price)
FROM fake_apps;
```


## AVG
It returns the average of a particular column
- It takes a name of a column as an argument
- It sums all the values in that column
- It divides the sum by the number of rows 
- It returns the average

```sql  
SELECT AVG(downloads)
FROM fake_apps; 
```

## ROUND
- It takes two arguments inside the parenthesis
  - A column name 
  - An integer
- It rounds the values in the column to the number of decimal places specified by the integer.

```sql
SELECT ROUND(price, 0)
FROM fake_apps;
```



## GROUP BY
Oftentimes, we will want to calculate an aggregate for data with certain characteristics. 
Group by helps by simplifying the work of repeating a task multiple times. Not like a loop but it is similar.
- Is used in collaboration with the select statement to arrange identical data into groups 
- Comes after any where statements, but before order by or limit

We can use group references that makes our code easily to read and better. 
- 1 is the first column selected
- 2 is the second column selected
- 3 is the third column selected


## HAVING
In addition to being able to group data using group by, SQL allow us to filter which groups to include and which to exclude. 
- When we want to limit the results of a query based on values of the individual rows, use where 
- When we want to limit the results of a query based on an aggregate property, use HAVING


## TIMESTAMP
Helps by formatting dates and times. We use the function strftime().
- It takes two arguments:
  - The format type
    - %Y returns the year (YYYY)
    - %m returns the month
    - %d return the day of the month 
    - %H returns 24-hour clock
    - %M returns the minute
    - %S returns the seconds
  - The column name
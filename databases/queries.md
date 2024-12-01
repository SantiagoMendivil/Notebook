# Table of contents 
- [Table of contents](#table-of-contents)
- [Queries](#queries)
  - [What are queries?](#what-are-queries)
  - [SELECT](#select)
  - [AS](#as)
  - [DISTINCT](#distinct)
  - [WHERE](#where)
  - [LIKE](#like)
  - [IS NULL](#is-null)
  - [BETWEEN](#between)
  - [AND](#and)
  - [OR](#or)
  - [ORDER BY](#order-by)
  - [LIMIT](#limit)
  - [CASE](#case)

# Queries 
## What are queries?
Queries allow us to communicate with the database by asking questions and returning a result set with data relevant to the question. 

## SELECT 
Select Is used every time you want to query data from a database. It is followed by * (meaning all) or a column.

```sql
SELECT column1, column2
FROM table_name 
```

## AS
Serves as an alias while renaming a column in the select.

```sql
SELECT name AS 'Titles'
FROM movies 
```

The output instead of being the name of the column, it will be the alias 'Titles' that we gave. 

NOTE: The alias will only rename the column in the query, but not in the table

## DISTINCT
Return unique values in the output. It filters out all duplicate values in the specified column(s).

```sql
SELECT DISTINCT tools 
FROM inventory; 
```


## WHERE
We can restrict our query results in order to obtain only the information we want. 

```sql
SELECT * 
FROM movies 
WHERE imdb_rating > 8;
```


The where clause filters the result set to only include rows where the condition is true. 





## LIKE 
It can be useful when looking for an specific value in the where clause.

```sql
SELECT * 
FROM movies 
WHERE name LIKE 'Se_en';
```

Like is a special operator used with the where clause to search for a specific patter in a column 

Percentage sign
The percentage sign slices the results to what we specify in the order we specified it. 

```sql
SELECT * 
FROM movies 
WHERE name LIKE 'A%'
```

This query will filter all movies that starts with A



## IS NULL 
The is null or is not null operator helps by knowing which values have a null value and which don't

```sql
SELECT name 
FROM movies 
WHERE imdb_rating IS NOT NULL;
```

This will filter the output to just query the movies that have an imdb rating. Those who don't have an imdb rating will be excluded. 


## BETWEEN
- Is used in the where clause to filter an output within a certain range. 
- Needs two arguments 
- Between the arguments you have to write the logical operator AND

```sql
SELECT * 
FROM movies 
WHERE name BETWEEN 'A' AND 'J';
```

This query will filter the movies which names start between the letter A and J.



## AND 
We use it to combine multiple conditions in a where clause to make the result more specific. 

```sql
SELECT * 
FROM movies 
WHERE year BETWEEN 1990 AND 1999 
    AND genre = 'romance';
```

This query will output all the movies in the 90's that were a romance movie 


## OR
Outputs a row if any of the conditions is true. 

```sql
SELECT *
FROM movies 
WHERE year > 2014
    OR genre = 'action';
```

This query will output all the movies that were made after the year 2014 and also will output all the movies that are action movies. 



## ORDER BY 
We can sort the results using order by, either alphabetically or numerically. We can sort the results either in ascending or descending order.

These instructions come after the column that we are ordering by. 
ASC: Ascending order
DESC: Descending order 

NOTE: Order by comes always after the where clause.

```sql
SELECT name, year, imdb_rating
FROM movies 
ORDER BY imdb_rating DESC;
```


## LIMIT
Limit is a clause that lets you specify the maximum number of rows the result set will have. 
NOTE: The limit clause comes always at the end of the query.

```sql
SELECT name, year, imdb_rating
FROM movies 
ORDER BY imdb_rating DESC;
LIMIT 3;
```

This query will output the top 3 movies with the higher imdb_rating.

## CASE 
A case statement allows us to create different outputs. The case statement comes in the select clause.
It is like an if statement in programming.

```sql
SELECT name,
    CASE
        WHEN imdb_rating > 8 THEN 'Fantastic'
        WHEN imdb_rating > 6 THEN 'Poorly Received'
        ELSE 'Avoid at All Costs'
    END AS 'Rates'
FROM movies;
```
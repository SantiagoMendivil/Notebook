# Table of contents 
- [Table of contents](#table-of-contents)
- [Subqueries](#subqueries)
  - [Inserts, updates, and deletes](#inserts-updates-and-deletes)
  - [Comparison operators](#comparison-operators)
  - [EXISTS / NOT EXISTS](#exists--not-exists)

# Subqueries
A subquery is an internal query nested inside of an external query. They can be nested in:

- SELECT
- INSERT
- UPDATE
- DELETE

Example:
If we have two tables, one of the book club of a school and the other of the art club, in order to find out which students are in both tables we can use a JOIN statement

```sql
SELECT id, first_name, last_name
FROM book_club
JOIN art_club
    ON book_club.id = art_club.id;
```    

This can be accomplished with a subquery like this:

```sql
SELECT id, first_name, last_name
FROM book_club
WHERE id IN (
    SELECT id
    FROM art_club
);
```

Let's break this code down:
1. In order of operations, the subquery will be executed first. It will display all id's from the art club.
2. Then the outer query will be executed, looking for all the statements in the select where the id of the book club appears in the id's of the art club.

As you notice, the output will be the same as the join, but it is more readable. 


## Inserts, updates, and deletes
We can use the same structure of a subquery to delete specific rows of a table

```sql
DELETE FROM drama_students
WHERE id IN (
  SELECT id
  FROM band_students
);
```

In this code we are deleting the students from the drama club that are also in the band club.

## Comparison operators
We can also use the comparison operators to filter the results of a query following a condition 

```sql
SELECT * 
FROM history_students
WHERE grade <= (
  SELECT grade
  FROM statistics_students);
```

This code for example is looking for the history students where the grades are less or equal to the grade of the statistics students.

NOTE: When using comparison operators, the statement that will be compared in the outer query must be the same as the one that we are selecting in the inner query.


## EXISTS / NOT EXISTS
Its functions are almost the same as the IN and NOT IN, but the difference is that the EXISTS statements are efficiently better than the IN statements, this is because the IN statements return all rows meeting the specific criteria, whereas the EXISTS statements only need to find the presence of one row to determine if a true or false value needs to be returned.

NOTE: It is not necessary to write the column that you're looking for in the where clause. 
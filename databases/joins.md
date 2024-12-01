# Table of contents
- [Table of contents](#table-of-contents)

# Multiple Tables
## JOIN ON
The easiest way to combine multiple tables into only one result.

```sql
SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id 
```

What we are saying here is that the customer id on the orders table, has to be the same in the customers table with the same name. In other words: 

1. The second line specifies the first table that we want to look in
2. The third line uses JOIN to say that we want to combine information from orders with customers
3. The fourth line tells us how to combine the two tables. We want to match order table's customer_id column with customers table's customer_id column.
    
In order to reference the table in which we are collecting and matching data, we use the table's name before a dot and then the column's name


## INNER JOIN
The inner join only queries the rows in the table that have a match in the other table. In the simple join this can't be done.

NOTE: Use INNER JOIN when you think or know that the data won't completely match. 

NOTE: This kind of join can be used for example with subscriptions. Maybe a user has 3 subscription's options, and at the end he only subscribes to one of them.


## LEFT JOIN 
If we want to combine to tables but keep some of the unmatched elements, we can use the left join to join two tables and if there are no matches in one of the rows, we can keep the info in the left table.

```sql
SELECT *
FROM newspaper
LEFT JOIN online
    ON newspaper.id = online.id
```

We write in the FROM statement the table that we want to keep all values

NOTE: Use this when we want to combine two tables and keep all information from one of them, in this case, the left table.

NOTE: If the condition is not met, the columns in the right table will be filled with NULL values.



## PRIMARY KEY VS FOREIGN KEY
- Every column that uniquely identifies a table is known as PRIMARY KEY.
- Every column that references the primary key of a table in other table is known as FOREIGN KEY

### Primary keys
- None of the values can be NULL
- Each value must be unique
- A table cannot have more than one primary key column 

### Foreign keys
It must reference correctly to the primary key of the table referenced. 


## CROSS JOIN 
It combines all rows from a table with all rows from another table. It helps when we want to know all possible combinations when comparing two tables.

```sql
SELECT shirts.shirt_color, pants.pants_color
FROM shirts
CROSS JOIN pants;
```

This query will select only the shirt color from the shirts table and the pants color from the pants table. And then it will be combining every single one of the shirts table rows and combine it with all of the rows in the pants table.


## UNION 
The union helps us when we have two tables with the same columns. In order to join these two tables and see all the rows, we use the union statement.

```sql
SELECT *
FROM table1
UNION
SELECT * 
FROM table2; 
```


SQL strict rules when appending data:
- Tables must have the same number of columns
- The columns must have the same data types in the same order as the first table.


## WITH
- The with statement allows us to perform a separate query.
- We specify an alias that we will use to reference any columns from the query inside the with clause
- Then we can do whatever we want with this temporary table(such as join the temporary table with another table).
    
```sql
WITH previous_query AS(
  SELECT customer_id,
    COUNT(subscription_id) AS 'subscriptions'
  FROM orders 
  GROUP BY customer_id
)
SELECT customers.customer_name,
  previous_query.subscriptions
FROM customers
JOIN previous_query
  ON previous_query.customer_id =
    customers.customer_id;
```


In this query instead of looking into the customer's id's, we are joining a whole new table in the with clause with another table in order to see the name of the customers that have a subscriptions. 
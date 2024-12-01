# Table of contents
- [Table of contents](#table-of-contents)

# Indexes 
## What are indexes? 
An index is an organization of the data in a table to help with performance when searching and filtering records. A table can have zero, one, or many indexes. 
It's important to know that indexes can be very costful when inserting, updating or deleting information from a table, this is because when having an index, these statements will be affected by the new info and slow down the process. So if you have an index, drop it, add the info or whatever you need to do, and then build up again the index

In order to see if the indexes exist in a table we must access them by writing: 

```sql
SELECT *
FROM pg_Indexes
WHERE tablename = 'table_name';
```

With this query we would see all of the indexes of the table that we call. 


## What is the benefit of an index? 
Indexing allows us to organize our database structure in such a way that it makes finding specific records much faster. By default it divides the possible matching records in half, then half, then hald and so on until the specific match you are searching for is found. This is known as a Biary Tree.


### Impact of indexes

```sql
EXPLAIN ANALYZE SELECT *
FROM table_name;
```

Running this query, it will return the plan that the server will use to give you every row from every record from a table


## CREATE INDEXES
If we wanted to create an index called customer_index on the customers table on the user_name column, this would be the code to implement this. 

```sql
CREATE INDEX customer_index ON customers(user_name);
```

And if it is multiple column, for example when two or more columns are always associated

```sql
CREATE INDEX customer_last_name_first_name_idx ON customers(last_name, first_name)
```

## Index Filtering
Queries that filter data often use WHERE and ON clauses. 


## Drop and Index
```sql
DROP INDEX IF EXISTS index_name
```

## Size of tables
```sql
SELECT pg_size_pretty
(pg_total_relation_size('tablename'));
```
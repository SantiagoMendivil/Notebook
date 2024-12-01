# Table of contents
- [Table of contents](#table-of-contents)

# Keys 
## What are the Keys? 
A database key is a column or group of columns in a table that uniquely identifies a row in a table.

## Why do we need Keys? 
Keys enable a database designer to place constraints on the data in a table. 

A primary key will ensure that each row in a table is unique.
A foreign key is the primary key of one table represented in another table


## Primary Key
A primary key is a designation that applies to a column or multiple columns of a table that uniquely identifies each row in the table. 

### Functionality
Designating a primary key on a particular column in a table ensures that this column data is always unique and not null. 

```sql
CREATE TABLE recipe (
  id integer PRIMARY KEY,
  name varchar(20),
  ...
);
```

This is the correct form to specify a primary key.

## Key Validation
### Information Schema

```sql
SELECT
    constraint_name, table_name, column_name
FROM 
    information_schema.key_column_usage
WHERE 
    table_name = 'some'
```

This code let us find out the constraints that have been placed on certain columns in a table, such as "some".

### Composite Primary Key
If the information can't be set as primary key by its own, we can group together couple of columns in order to set the combination of those columns into the primary key

```sql
PRIMARY KEY (column_one, column_two)
```
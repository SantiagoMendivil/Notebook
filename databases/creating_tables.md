# Table of contents 
- [Table of contents](#table-of-contents)

# Creating Tables 
## Creating your tables

```sql
CREATE TABLE name_of_table (
    Data varchar(size_of_varchar),
    Data2 integer,
    Data3 money
);
```

CREATE TABLE: Specifies that we are creating a table
name_of_table: The name of the table, specified by you
data: Separated by commas and everyone has a datatype


## Querying your tables

### Insert data into tables

```sql
INSERT INTO name_of_table VALUES (
    column_one value,
    column_two value,
    .
    .
    .
    column_N Value
);
```

### Relationships Between Tables 
In order to make a connection between two entities we have to add a constraint to those entities. For example, we have an entity called person and another one called email. A person could have more than one email, but an email belongs to only one person. So, we need to apply the constraint on the email table by adding another column to it and designating it to associate with the person table. 

# Table of contents
- [Table of contents](#table-of-contents)
- [Constraints](#constraints)
  - [Nullability Constraints](#nullability-constraints)
  - [Improving Tables with Constraints](#improving-tables-with-constraints)
  - [Check Constraints](#check-constraints)
  - [Check Constraints Continued](#check-constraints-continued)
  - [Unique Constraints](#unique-constraints)
  - [Introduction to Primary Keys](#introduction-to-primary-keys)
  - [Introduction to Foreign Keys](#introduction-to-foreign-keys)
  - [Foreign Keys - Cascading Changes](#foreign-keys---cascading-changes)
    - [Delete or update all references from a child table from a single key](#delete-or-update-all-references-from-a-child-table-from-a-single-key)

# Constraints
## Nullability Constraints
Use this constraint in order to prevent null spaces in the INSERT INTO statement.

```sql
CREATE TABLE talks (
    id integer,
    title varchar NOT NULL,
    speaker_id integer NOT NULL,
    estimated_length integer,
    session_timeslot timestamp NOT NULL
);
```

By doing this, you'll ensure that the columns must receive a value in order to continue.


## Improving Tables with Constraints
We can use ALTER TABLE to add or remove constraints. 
This helps us when we already filled a table with values. We can achieve this by doing the following: 

```sql
ALTER TABLE talks
ALTER COLUMN session_timeslot SET NOT NULL;
```

In that code, session_timeslot is the column name that the constraint will be applied to.
On the other hand, if we want to delete that constraint we can do:

```sql
ALTER TABLE talks
ALTER COLUMN session_timeslot DROP NOT NULL
```

NOTE: If we want to add the constraint it will raise an error because the table is already filled with null values, so we can do:

```sql
UPDATE talks
SET title = 'TBD'
WHERE title IS NULL;
```

In order to drop the null values with placeholders, and then now we can actually add the constraint.

## Check Constraints
A check constraint can be written into a CREATE TABLE statement, or added with ALTER TABLE. 
We have to write the reserved word CHECK and the logical statement. 

```sql
ALTER TABLE talks 
ADD CHECK (estimated_length > 0);
```

In the code example we are verifying that the estimated length of the column in the table is a possitive value. And in order to do the same but directly in the create table statement, we have to do:

```sql
estimated_length integer NOT NULL CHECK (estimated_length > 0)
```

## Check Constraints Continued 
Inside a check statement we can use a wide array of SQL syntax to create our conditions. 

- Make comparison between columns within the table 
- Use logical operators like AND and OR
- Use other SQL operators you may be familiar with (IN, LIKE)

For example:

```sql
ALTER TABLE talks 
ADD CHECK (estimated_length > 0 AND estimated_length < 120);
```

Another example can be that a talk must last less that 120 minutes and also it needs to be after the year 2020

```sql
ALTER TABLE talks
ADD CHECK (estimated_length < 120 AND date_part('year', session_timeslot) = 2020);
```

NOTE: The date_part function returns a portion of the date as an integer. 


## Unique Constraints 
In orderd to create a column to be unique, we can just add the UNIQUE statement at the end of the column declaration. But we can also do it in the alter table.

```sql
ALTER TABLE attendees 
ADD UNIQUE (email);
```

In this case we have to alter the table in which the column is part of and then we have to write ADD UNIQUE and the name of the column that we want to specify. 

## Introduction to Primary Keys
A primary key is a column (or set of columns) that uniquely identifies a row within a database table. A table can only have one primary key.
The column must have the following points in order to be considered as primary key.

- Uniquely identify that row in the table (like a UNIQUE constraint)
- Contain no null values (like a NOT NULL contraint)\

```sql
ALTER TABLE attendees
ADD PRIMARY KEY (id);
```

Adding a primary key is like setting  NOT NULL and UNIQUE to a column. 


## Introduction to Foreign Keys

```sql
ALTER TABLE registrations
ADD FOREIGN KEY (talk_id)
REFERENCES talks (id);
```

This would act the same as we declare the foreign key in the creat table statement. 


## Foreign Keys - Cascading Changes
### Delete or update all references from a child table from a single key
By default a foreign key will prevent an engineer from deleting or updating a row of a parent table that is referenced by some child table. This can be explicitly specified in a CREATE TABLE  using 

```sql
REFERENCES  talks (id) ON DELETE RESTRICT or REFERENCES talks (id) ON UPDATE RESTRICT
```

Instead of doing this, we can apply a CASCADE. Rather than preventing changes CASCADE clauses (ON UPDATE CASCADE, ON DELETE CASCADE) cause the updates or deletes to automatically be applied to any child tables. 

```sql
ALTER TABLE registrations
ADD FOREIGN KEY (talk_id)
REFERENCES talks (id) ON DELETE CASCADE
```

This code would force the id from the talks table to remove all instances that it has referenced to it. 
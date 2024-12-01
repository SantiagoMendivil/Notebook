# Table of contents
- [Table of contents](#table-of-contents)
- [Relationships](#relationships)
  - [ONE TO ONE](#one-to-one)
  - [ONE TO MANY](#one-to-many)
  - [MANY TO MANY](#many-to-many)
    - [Considerations](#considerations)

# Relationships 
## ONE TO ONE
We have two tables. One for a driver and another for its license.
The driver has 
- name
- address
- date_of_birth
- license_id
The license has
- id
- state_issued
- date_issued
- date_expired
In this example a license has its own unique identifier, and the driver has an associated license to it by setting the license id equal to the id of the license. In order to join these two tables we have to declare a foreign key in:

```sql
license_id char(20) REFERENCES driver(license_id) UNIQUE
```


## ONE TO MANY
We need to have in mind that if we want to use a one-to-many relationship, it is because one of the tables can have more than one element of the foreign key. 

## MANY TO MANY
Both tables can have more than one row of their foreign keys. For example
- A student can take many courses while a course can have enrollments from many students
- A recipe can have many ingredients while an ingredient can belong to many different recipes 
- A customer can patronize many banks while a bank can service many different customers. 

### Considerations
- When having a relationship like one of the above, consider creating an auxiliar table in order to save the matches there, obviously setting the foreign and primary keys well. 
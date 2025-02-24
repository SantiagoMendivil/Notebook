# Table of contents
- [Table of contents](#table-of-contents)
- [Manipulation](#manipulation)
  - [ls, revisited](#ls-revisited)
  - [ls \& combining options](#ls--combining-options)
  - [cat](#cat)
  - [cp](#cp)
  - [Wildcards](#wildcards)
  - [mv](#mv)
  - [rm](#rm)
    - [-r](#-r)
    - [-f](#-f)

# Manipulation
## ls, revisited 
This ls command lists all files and directories in the working directory with more detail. 

- -a: Lists all contents, including hidden files and directories.
- -l: (a lowercase L) lists all contents of a directory in long format, as well as the file permissions
- -t: Orders files and directories by the time they were last modified
- -alt: Lists all contents, including hidden files and directories, in long format, ordered by the date and time they were last modified



## ls & combining options
The -l options lists files and directories as a table. Here's what each column means:
1. Access rights. These indicate the read, write and execute permissions on the file or directory allowed to the owner, the group, and all users.
2. Number of hard links. This represents the numbers of hard links to the file or directory. This includes the parent directory (..) and the current directory (.)
3. The username on the file's owner. 
4. The name of the group that owns the file. 
5. The size of the file in bytes
6. The date & time that the file was last modified. 
7. The name of the file or directory
    
    
    
## cat 
This command prints the content of a file in the terminal of Bash. Taking as an example the file from the echo example: 

```bash
cat hello_cli.txt
```

This will print in the terminal "Hello Command Line"
We can also print files inside a directory by calling first the directory and then the file

```bash
cat directory_name/file.txt
```

## cp
CP stands for copying, moving and removing files and directories from the command line

```bash
cp source.txt destination.bak
```
This example copies the first file into a new file or an existing one that is the second file. 

**NOTE**: The .bak extension is commonly used to notate a file as a backup of a file with the same name. 

We could also copy a file into a directory by following the same structure, but in this case, replacing the second argument with the directory name. 
**NOTE**: If we want to rename the file we use the same structure but we need to include the name in the path of the second argument.

```bash
cp file.txt folder/new_name.txt
```

We could copy more than one file by adding the files in the same line and the destination at the end

```bash
cp file1.txt file2.txt destination/
```

## Wildcards
1. cp *: The asterisk symbol would copy all files from a directory into another directory.
2. cp *.extension: The asterisk with a dot and then the type of extension would copy only the files with that extension and move them into the new directory.
3. cp w*.extension: The w before the last wildcard selects all files in the directory starting with the letter w and ending with the extension in order to copy them into the directory.


## mv 
This command works almost the same as cp but instead of making a copy it just moves the file into a new directory 


## rm
Removes files and directories. 

### -r
If we add -r to the rm command we will delete in a recursive way all the directory and its child directories.
NOTE: Once a file or directory is removed, it won’t be recovered.

### -f  
Will delete forcibly without individually confirming each piece of content inside the directory. It can be combined with -r and create a -rf deleting object. 
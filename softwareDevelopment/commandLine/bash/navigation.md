# Table of contents
- [Table of contents](#table-of-contents)
- [Navigation Commands](#navigation-commands)
  - [ls](#ls)
  - [pwd](#pwd)
  - [cd](#cd)
  - [mkdir](#mkdir)
  - [touch](#touch)
  - [echo](#echo)

# Navigation Commands
## ls
This command means 'lists', so when we type it, the command line looks at the directory you are in, and then lists all the files and directories inside of it. 

```bash
ls
```

The terminal would display the current directory and its files and directories. 


## pwd
This command means "print working directory". It outputs the name of the directory you are currently in, called the working directory. This command goes before the ls command. 

```bash
pwd
```

The terminal would display the current path for the directory. 


## cd
This command stands for "change directory". Basically it switches the current directory to the one specified in the command. 
The cd command takes a directory name as an argument. 

```bash
cd directory_name
```

- If we type only two points after the cd we will get back to the directory above the current working directory 

```bash
cd ..
```
- If we are going to move more than one file we can make all the moves in only one line dividing the directories with forward slashes /

```bash
cd directory1/directory2
```
- This also can be done with double points to reference the folder above

```bash
cd ../..
```

NOTE: use double points always that you want to move to an adjacent directory.


## mkdir
This command stands for "Make directory". It takes in a directory name as an argument and then creates a new directory in the current working directory.

```bash
mkdir media
```

This command would create a new directory called media inside the working directory

In order to make a new directory in a directory inside the current one we only need to add a forward slash to specify it

```bash
mkdir media/tv
```

## touch 
Touch is used to make files inside a directory. This command creates a new file inside the working directory. It takes a filename as an argument and then creates an empty file with that name in the current working directory. 

```bash
touch one_file.txt
```


## echo
Prints something inside an existing file. You need to specify the text inside double quotes and then point to the file which you want to add that text into.

```bash
echo "Hello Command Line" >> hello_cli.txt
```

This will add the text of "Hello Command Line" into the file hello_cli.txt
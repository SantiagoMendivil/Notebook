# Table of contents
- [Table of contents](#table-of-contents)
- [Redirection](#redirection)
  - [\> command (redirect stdout)](#-command-redirect-stdout)
  - [\>\> command (append)](#-command-append)
  - [\< command](#-command)
  - [| command](#-command-1)
  - [sort](#sort)
  - [uniq](#uniq)
  - [grep](#grep)
    - [Matching filenames and lines](#matching-filenames-and-lines)
    - [Matching filenames without lines](#matching-filenames-without-lines)
  - [sed](#sed)

# Redirection 
## > command (redirect stdout)
The > command redirects the standard output to a file. Basically overwrites information from a file into another one.

```bash
echo "Hello" > hello.txt
```

This command redirects the text "Hello" to a file called hello.txt.
Also we can redirect the information from a file into another one.

```bash
cat file1.txt > file2.txt
```

This sends the output of the file 1 into the file 2.


## >> command (append)
The >> command adds information from a file into another one or information that you specify into another one. Basically works like the append function of a list.

```bash
$ cat forests.txt >> hello.txt
```

This command will add the information in forests.txt into the hello.txt file

## < command
This command takes the standard input from the file on the right and inputs it into the command on the left. 

```bash
cat < file1.txt
```

## | command
| is a "pipe". This command takes the standard output of the command on the left, and pipes it as standard input to the command on the right. 

```bash
cat volcanoes.tx | wc
```

This command would return the word count (wc) from the file volcanoes.txt.
We can chain multiple pipes in order to make a bigger consult. 

```bash
$ cat volcanoes.txt | wc | cat > count.txt
```

In this example we get the output of volcanoes.txt, then we count the words in it, and finally we pass it all to the count.txt file. 


## sort 
The sort command takes a file as an argument and sort the information inside alphabetically but just in the output. It doesn't change the file itself. 
We can assign the result into another file by using the command >

```bash
sort file.txt > another_file.txt
```


## uniq
Filters out the duplicates and return only unique values. An efficient way to use uniq is by calling first the sort command in order to find the duplicates easily, and then join that sorted list with a pipe to the uniq command. We can add the results to another file as well.

```bash
sort file.txt | uniq > another_file.txt
```

## grep 
Stands for "global regular expression print". It searches files for lines that match a pattern and then returns the results. 

```bash
grep America continents.txt
```

This command line would return if the text America is included in the continents.txt. 
**NOTE**: The grep command is case sensitive, so use -i in order to avoid the case sensitive letters and focus on the word.

### Matching filenames and lines
If we add -R the command will search all files in a directory and output the filenames and lines containing matched results. -R stands for recursive. 
**NOTE**: To search something in the current location we can use the dot notation. 

### Matching filenames without lines
If we add -Rl (lowercase L) it searches all files in a directory and outputs only filenames with matched results (no lines).

## sed
Sed stands for stream editor. It accepts standard input and modifies it based on an expression, before displaying it as output data.

```bash
sed 's/snow/rain' forests.txt
```

This command show us:
- s: stands for substitution . It is always used when using sed command.
- Snow: the search string, or the text to find 
- Rain: The replacement string, or the text to add in place

**NOTE**: That command only replaces the first word that it founds. In order to replace all the words that match we need to add a fourth argument with the letter 'g' standing for global.
**NOTE**: This replacement only replaces the words in the output but not in the actual file. If we want to modify the real file we have to add the -i command.


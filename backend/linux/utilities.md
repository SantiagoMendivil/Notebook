# Table of contents 
- [Table of contents](#table-of-contents)

# Linux Shell Utilities 
## Access Documentation in Linux
We can access documentation in the terminal itself using these files and commands: 

- The `/usr/share/doc` directory 
- The `man` command 
- The `info` command

### `/usr/share/doc`
This directory contains README files, simple text files that describe a program, for many installed packages in your Linux distribution. 

We can explore the documentation by using this command: 

```bash
ls /usr/share/doc
```

To read a specific file, you can use `cat`, `less`, or any text editor. For example:

```bash
cat /usr/share/doc/bash/README
```

### The `man` command 
This is used to access the manual pages, the traditional way of distributing documentation for all bash programs. The command 

```bash
man [options] <command_name>
```

will give us the command's manual page, which includes a brief synopsis of the program, a description that lists all options, and examples.

For example, `man cat` will display the manual page for the command `cat`. Another example is `man ls`, which will show the manual page for the `ls` command.

#### Sections in `man` pages
The `man` pages are divided into sections, each providing different types of information. The common sections include:

1. **NAME**: The name of the command or function, followed by a brief description.
2. **SYNOPSIS**: A summary of how to use the command or function.
3. **DESCRIPTION**: A detailed description of the command or function.
4. **OPTIONS**: A list of options that can be used with the command or function.
5. **EXAMPLES**: Examples of how to use the command or function.
6. **SEE ALSO**: References to related commands or functions.

You can specify the section number to view a specific section of the manual. For example:

```bash
man 5 passwd
```

This command will display the manual page for the `passwd` file format (section 5), rather than the `passwd` command (section 1).

Another example is:

```bash
man 3 printf
```

This will show the manual page for the `printf` function in section 3 (library functions).

#### Searching within `man` pages
You can search for specific keywords within a `man` page by typing `/` followed by the keyword and pressing `Enter`. To navigate through the search results, press `n` for the next result and `N` for the previous result.

For example, to search for the keyword "option" in the `man ls` page:

```bash
man ls
/option
```

#### Navigating `man` pages
- Press `Space` to move to the next page.
- Press `b` to move to the previous page.
- Press `q` to quit the `man` page.

#### Getting help with `man`
If you need help with using the `man` command itself, you can access its manual page by typing:

```bash
man man
```

Another useful command is `man -k <keyword>`, which searches the manual page names and descriptions for the keyword. For example:

```bash
man -k copy
```

This will list all manual pages related to the keyword "copy".


### The info command
Even though manual pages are somewhat outdated, they make for great sheets/reference cards. We can use the info command which also contains more recent information about programs than man. Its usage is: 

```bash 
info [options] <command_name> 
```

#### Navigating `info` pages
- Press `Space` to move to the next page.
- Press `b` to move to the previous page.
- Press `n` to move to the next node.
- Press `p` to move to the previous node.
- Press `u` to move up a level in the node hierarchy.
- Press `q` to quit the `info` page.

#### Searching within `info` pages
You can search for specific keywords within an `info` page by typing `s` followed by the keyword and pressing `Enter`. To navigate through the search results, press `s` again.

For example, to search for the keyword "option" in the `info ls` page:

```bash
info ls
s option
```

#### Getting help with `info`
If you need help with using the `info` command itself, you can access its help page by typing:

```bash
info info
```

Another useful command is `info --apropos <keyword>`, which searches the `info` pages for the keyword. For example:

```bash
info --apropos copy
```

This will list all `info` pages related to the keyword "copy".
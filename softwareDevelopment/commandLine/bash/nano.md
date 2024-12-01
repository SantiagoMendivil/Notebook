# Table of contents 
- [Table of contents](#table-of-contents)

# Nano
## What is Nano? 
- Nano is a command line text editor.
- It only accepts keyboard input.
- It works the same way as a desktop text editor 
- In order to open a new text file we have to write "nano" and then the filename.

## The most important commands
ctrl + o: Writes the lines in nano into the file that is opened 
ctrl + x: Exits the nano command line text editor 


## Customization with bash_profile
We need to work with the bash_profile in the starting directory, not the home directory

In order to open the customization we need to write

```bash
nano .bash_profile 
```

Once inside the bash profile, we can add commands to execute every time a new terminal session is started. 
In order to activate the changes made in .bash_profile we have to write the command:

```bash
source .bash_profile
```

## Aliases
The alias command allows you to create keyboard shortcuts, or aliases, for commonly used commands. For example: 

```bash
alias pd="pwd"
```

Here we create the alias pd for the pwd command, which is then saved in the bash profile. We need to make sure that we update the source .bash_profile to save the changes. 

**NOTE**: We can add aliases to complete commands just as ls -la. 

```bash
alias el="ls -la"
```

## Environment variables

```bash
export USER="Santiago"
```
Command line that let us know who is the computer's owner

```bash
export PS1=">> "
```

PS1 is an environment variable that defines the makeup and style of the command prompt.
This command line will change the command prompt from $ to >>, so when we use the source command, this will be displayed 

```bash
echo $HOME
```

The home variable is an environment variable that displays the path of the home directory ~. The ~ means home

```bash
echo $PATH
```

Path is an environment variable that stores a list of directories separated by a colon. 

```bash
env
```

Returns the environment variables for the current user.

To return every one of this variables we have to echo and then $variablenann
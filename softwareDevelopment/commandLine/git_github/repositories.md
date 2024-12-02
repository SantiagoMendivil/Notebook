# Table of contents 
- [Table of contents](#table-of-contents)

# Clone Repositories
## How can we clone a repository from GitHub?
In order to accomplish this, we need to follow the next steps:

1. Go into GitHub and look for the repository you want to clone.
2. Once you are there, you must click on the button Code
3. It will appear an HTTPS extension. Copy that extension
4. Then go to Git Bash and navigate into the directory where you want to save the repository.
5. Then write the command git clone <extension> in order to copy the files from the repository into a new project in this folder
    
At this point you already have cloned a repository from GitHub. We could make changes and modify the files but this is bad practice. We have to create a new branch in order to not affect other people working on this file. How?

1. Navigate into the cloned project and verify that the files are there
2. Once you've done this, write the command git checkout -b print_changes
   1. This line will create a new branch called 'print_changes' for the current project
   2. The name is arbitrary
3. To modify the new branch we have to access nano and specify the name of the file.
4. To create new files in the project we can also call nano and then the file name that you want

## Special commands
```bash
git add .
``` 
Adds all the files to the staging area

```bash
git status
```
Outputs the actions we've been doing

```bash
git commit -m "message with changes"
```
Commit the changes in the files and leaves a message specifying which were the changes
    
```bash
$ git push --set-upstream origin print_changes
```
The name print_changes depends on the file of GitHub. This command submits the new branch into the repository of GitHub. It doesn't affect the original one.
    
## Pull request 
In GitHub, navigating into the branches of the project, we can set a branch as the new original one by pulling a new request on the branch you want. 
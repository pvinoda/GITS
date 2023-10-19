# About gits commit
This command is used to commit changes present inside the staging area. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_commit.py).

# Code Description
## Functions
1. gits_commit_func(args):
this function takes **args** object as an input which has an attribute **m** to store the commit message and another boolean attribute **amend**. 
To increase convenience, the user is allowed to use a set of default commit messages by using "1" and "2" as the commit message.
If **amend** is set to true, command will not create new commit. Instead, it will simply add changes to the last commit.
Function returns True for successful execution and False otherwise with an exception.


# How to run it? (Small Example)
Let say you are on a particular branch working on some feature X. 
You've made some changes so far and you want to commit those chnages.
You can use the following command to do so:
```
$ gits commit -m "My first commit"
```
Let's say you're updating your Readme.md file very often or you want you want to add empty log message.
You can use the following modification of the above commit command:
```
$ gits commit -m "1" (Update Readme.md)
$ gits commit -m "2" (*** empty log message ***)
```

Soon after you realized a mistake in the last commit and want to fix that mistake.
However you do not want others to notice that mistake. 
In this situation, you can use the amend argument as shown below to update the last commit.
```
$ gits commit -m "My first commit with mistake fixed" --amend
``` 
After successful execution of this command, you will still have only one commit for the changes you have made so far.
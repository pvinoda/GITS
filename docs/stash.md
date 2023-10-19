# About gits stash
The stash command in Git is used to temporarily save changes that you have made in your working directory but do 
not want to commit yet. It allows you to set aside your changes and return your working directory to the last committed 
state. 

# Location of Code
The code that implements the abovementioned gits functionality is located [here](https://github.com/pvinoda/GITS/blob/master/code/gits_stash.py).

# Code Description
The gits stash generates an input prompt that asks for a label. If no label is provided, it saves with a random stash ID.
The command git stash list is internally executed to display the corresponding results.
## Functions
1. gits_stash(args):
The `gits_stash` function is a Python script that simplifies Git stash management. It prompts users to label their 
stashes for identification and lists all stashes in the repository, making it easier to organize and manage changes.


# How to run it? (Small Example)
Use the command in following way to stash your changes. Respond to the prompts to store labels to your changes.
The state of your stash is immediately displayed so that you can visualize what's going on inside.
```
$ gits stash 
- Do you want to label your stash to identify the contents in future? (Y/N)
$ Y
- Please enter the message label now !!
$ stashing the documentation changes
- Here's what your current stash looks like..
(Entire stash displayed for maintenance purposes)

```
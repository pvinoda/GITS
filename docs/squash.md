# About gits squash
Squashing commits means combining multiple, often related, Git commits into a single commit with a cleaner and more 
concise commit history. This can be useful when you have a series of small, incremental commits that you want to 
consolidate into a more meaningful and comprehensible unit of work.

# Location of Code
The code that implements the abovementioned gits functionality is located [here](https://github.com/pvinoda/GITS/blob/master/code/gits_squash.py).

# Code Description
The Python function, `gits_squash`, is designed to automate the process of squashing the last 'n' commits into a 
single commit in a Git repository. It takes 'n' and a commit message as input, resets the branch to the desired commit, 
stages the changes, and creates a new commit with the specified message. It leverages the subprocess module to execute 
Git commands within a Python script.
## Functions
1. gits_squash(args):
The `gits_squash` function is a Python script that simplifies Git Squash operation helping to keep commit history very clean. 
It understands the number of commits that need to be squashed together, and does the deed by labelling the new commit with the
message provided by the user.

# How to run it? (Small Example)
Use the command in following way to squash your commits in a simple, yet flexible fashion.
```
$ gits squash -n 3 -m "the last three changes" 
- Squash completed. Please check your new git log now.
(The log will display a clean commit history that has squashed commits together before pushing to remote).
```
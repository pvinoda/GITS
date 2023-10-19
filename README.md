
# GITS 
### GIT Simplified

![GitHub](https://img.shields.io/github/license/harshitpatel96/GITS)
[![Build Status](https://travis-ci.com/harshitpatel96/GITS.svg?branch=master)](https://travis-ci.com/harshitpatel96/GITS)
[![codecov](https://codecov.io/gh/harshitpatel96/GITS/branch/master/graph/badge.svg?token=G6RG52G2YO)](https://codecov.io/gh/harshitpatel96/GITS/)
![YouTube Video Views](https://img.shields.io/youtube/views/6Y8_RQecnZ8?style=social)

[![DOI](https://zenodo.org/badge/295480790.svg)](https://zenodo.org/badge/latestdoi/295480790)

![GitHub issues](https://img.shields.io/github/issues/harshitpatel96/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/harshitpatel96/GITS)

![Lines of code](https://img.shields.io/tokei/lines/github/harshitpatel96/GITS)

[![](https://img.youtube.com/vi/6Y8_RQecnZ8/hqdefault.jpg)](https://youtu.be/6Y8_RQecnZ8 "GITS demo")

# About GITS
GITS streamlines most frequently performed workflows using fewer commands which is so much easier and better than usual.
Git-Simplified AKA GITS can be thought of wrapper around major Git functionalities.

# Installation for Linux
1. Clone GITS Repo
2. From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3. Go to configurations directory and run the following command

    If you are working on Linux system with a bash terminal or a Windows system using Windows subsystem for linux:
    ```
    bash project_init.sh
    ```
    If you are working on Linux system with a fish terminal:
    ```
    fish project_init.fish
    ```
4. Source the bashrc file
    ```
    source ~/.bashrc
    ```
    
    Note: Open the .bashrc file in User home directory to make sure that the alias command does not have any white spaces in the path. If so, rename the directory to remove the white spaces and re-run the setup.

# Installation for Windows
1. Clone GITS Repo
2. From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3. Currently, this project cannot be run on Windows. You need to make use of WSL to work on this project in Windows 
although this fix would only work for systems running Windows 10. If you are using another version of Windows, using a 
virtual machine might be preferred.

    Please refer this link to enable WSL : https://docs.microsoft.com/en-us/windows/wsl/install-win10

# How to Contribute?
Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and help us in enhancing the current video conferencing platforms.

# Documentation
## Functionalities Implemented
You can change the paths in your list of links to match the new format you provided. Here are the updated links:


1. [gits profile](https://github.com/pvinoda/GITS/blob/master/docs/profile.md)
2. [gits rebase](https://github.com/pvinoda/GITS/blob/master/docs/rebase.md)
3. [gits reset](https://github.com/pvinoda/GITS/blob/master/docs/reset.md)
4. [gits upstream](https://github.com/pvinoda/GITS/blob/master/docs/upstream.md)
5. [gits super reset](https://github.com/pvinoda/GITS/blob/master/docs/super_reset.md)
6. [gits commit](https://github.com/pvinoda/GITS/blob/master/docs/commit.md)
7. [gits create_branch](https://github.com/pvinoda/GITS/blob/master/docs/create_branch.md)
8. [gits logging](https://github.com/pvinoda/GITS/blob/master/docs/logging.md)
9. [gits undo](https://github.com/pvinoda/GITS/blob/master/docs/undo.md)
10. [gits untrack](https://github.com/pvinoda/GITS/blob/master/docs/untrack.md)
11. [gits track](https://github.com/pvinoda/GITS/blob/master/docs/track.md)
12. [gits delete](https://github.com/pvinoda/GITS/blob/master/docs/delete.md)
13. [gits sync](https://github.com/pvinoda/GITS/blob/master/docs/sync.md)
14. [gits switch](https://github.com/pvinoda/GITS/blob/master/docs/switch.md)
15. [gits status](https://github.com/pvinoda/GITS/blob/master/docs/status.md)
16. [gits branch](https://github.com/pvinoda/GITS/blob/master/docs/branch.md)
17. [gits diff](https://github.com/pvinoda/GITS/blob/master/docs/diff.md)
18. [gits init](https://github.com/pvinoda/GITS/blob/master/docs/init.md)
19. [gits merge](https://github.com/pvinoda/GITS/blob/master/docs/merge.md)
20. [gits push](https://github.com/pvinoda/GITS/blob/master/docs/push.md)
21. [gits pull](https://github.com/pvinoda/GITS/blob/master/docs/pull.md)
22. [gits stash](https://github.com/pvinoda/GITS/blob/master/docs/stash.md)
23. [gits squash](https://github.com/pvinoda/GITS/blob/master/docs/squash.md)

These links now point to the "master" branch instead of "phase2_se23_team71" in your GitHub repository.

I've changed the links to the new format you provided with the updated repository path and branch.



## Pydoc implementation
We have tried to write as much documentation as possible. You can use pydoc to go through the documentation. 
For example if you want to go through all the documentation for all files in code/ directory, do the following: 

`cd code`<br>
`python3 -m pydoc -b `

This will open up a browser and you can see all the files. You can click on a particular file to access the 
documentation associated with that file.

This repository is made for CSC 510 Software Engineering Course at NC State University.


## Experimentation setup for phase 3

This project aims to ease the developers efforts while interacting with version control system Git. 
Here are few motivation points behind coming up with this idea:
- Few git command names are very misleading from the end user's perspective. Consider this, ```git checkout``` command is used for both switching the branches and removing changes present inside working directory.
- Based on the development practice used by various teams, there are some tasks which requires the execution of more than one command to complete the task. This process can be easily automated such that developer only need to execute a single command to get their work done.
- There are almost always the cases that because of not much efficient syncing techniques, code pushed to the remote repository results in conflict while merging. It is always best practice to solve any such merge conflicts on the local repo rather than the remote one.

To solve the issues described above, we came up with the project **gits** that stands for **git-Simplified**.
So, this experiment aims to compare various aspects to traditional git and our proposed gits.

### Participation

Basic idea here is to let the participants finish the tasks present in the tasks list mentioned below, and observe whether gits made this process easier or not. 
This is higher level idea for this study.
There are two ways to choose who will use git and who will use gits.
1. If you have significant number of participants, you can divide them up into two groups. Participants from one group will use Gits to complete the set of tasks while participants from second group will use traditional Git to finish their tasks. 
to achieve some great results, participants with lesser git knowledge should be assigned to later group who will be using git to finish their task. That would lessen the bias in observations since people would be already familiar with git rather than gits.
2. If number of participants are limited and have enough time, you can let each participants finish the set of tasks twice. Once using traditional git and then using gits.
However, to remove any unwanted bias here as well, divide the participants in two groups. first group should use the git first and then gits. Second group should finish the tasks using gits first and then using git.

Ask each participants to setup the gits inside their local machine before starting the study using steps shown above.

### Tasks list
Here is basic draft of the tasks that covers almost each enhancement. 
Feel free to edit this list as per your convenience. Add few tasks if you got more time for the experiment.

- Create a test repository that can be used by participants to complete their tasks.
- Ask participant to clone the repository on their local machine.
- Ask participant to set their git profile name and email to "dummy_name" and "dummy@name.com" respectively. Once they are done, ask them to switch it back to the original ones.
- Create two branches with name: branch1 and branch2.
- list all the branches.
- From current branch, switch to the branch1.
- create a file named "foo.txt" and write some text in it.
- track the file "foo.txt" so that it gets considered for the next commit.
- Create another file named "bar.txt" and add some text in it.
- track this file "bar.txt" so that it gets considered for the next commit.
- commit these changes with appropriate commit message.
- make some change to the "bar.txt" and track those changes so that they get considered for the next commit.
- You found some issues with changes to this file and now you don't want it to be considered for the next commit. remove those changes from commit area.
- Also remove those changes from working directory.
- commit these changes with appropriate commit message and switch to the main branch.
- merge changes from the branch1 into this main branch and push those changes to the remote main branch.
- Now switch to branch2.
- Main branch has changed since we created this branch so this branch is working behind in changes. Make this branch up to date with local main branch.
- You just got to know that some other developer merged his changes to the remote main branch. Since you have checked out from the main branch, you also want those changes in development branch. So, make your branch up to date with remote main branch.
- Now switch to main branch again.
- create new file "temp.txt" and write some text in it and commit those changes.
- You just realized you directly made changes to the main branch rather than your development branch by mistake. Undo those changes by making current main branch same as remote main branch.
- You just got to know that someone merged their changes to the remote main branch. Sync your main branch.
- Last commit that is present in the main branch is not working well so you want to remove changes made by that commit entirely on both: local and remote.
- You are doing great till now but assume a hypothetical scenario where you have made a mess in your local repo and want to delete the current repo and fork it all again.


### Quantitative measures
Here are some measures that can help compare the results between traditional git and gits.
1. Time taken to finish a particular task.
2. Number of commands executed to complete each task.
3. Number of time participants referred to the documentation or any other resources.

### Qualitative measures
Along with quantitative measures described above, few qualitative measures can help to assess the performance better.
1. Familiarity with traditional git
2. hardness of the task

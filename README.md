
# GITS 
### GIT Simplified

![GitHub](https://img.shields.io/github/license/harshitpatel96/GITS)
[![Build Status](https://travis-ci.com/harshitpatel96/GITS.svg?branch=master)](https://travis-ci.com/harshitpatel96/GITS)
[![codecov](https://codecov.io/gh/harshitpatel96/GITS/branch/master/graph/badge.svg?token=G6RG52G2YO)](https://codecov.io/gh/harshitpatel96/GITS/)
![YouTube Video Views](https://img.shields.io/youtube/views/6Y8_RQecnZ8?style=social)

[![DOI](https://zenodo.org/badge/704961751.svg)](https://zenodo.org/doi/10.5281/zenodo.10023186)

![GitHub issues](https://img.shields.io/github/issues/harshitpatel96/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/harshitpatel96/GITS)

![Lines of code](https://img.shields.io/tokei/lines/github/harshitpatel96/GITS)

[![](https://github.com/pvinoda/GITS/blob/master/GITSvGIT.jpeg)](https://www.youtube.com/watch?v=b5-aySJRoMc "GITS demo")

## [Link to the Video Demo of GITS](https://www.youtube.com/watch?v=b5-aySJRoMc)
# The What??
## About GITS
GITS simplifies the often cumbersome and confusing commands of git to provide a user friendly experience to beginners in version control, as well as making it time efficient for proficient users. GITS also adds multiple features on top of git functionalities to provide a richer experience. 


# The Why ??

## Motivation
Git is the most popular version control system used by developers all around the world. Given its ubiquity, most newbies find it daunting to understand some of the commands in Git.
We aim to simplify some commands by make them more powerful by combining related commands into one intuitive command. We also alleviate confusion in some commands by making them more intuitive.
We hope that these features will help amateurs as well as experienced developers to use git. 

## Key features

1. ### Interactive GUI
   We provide a simple yet effective GUI which takes in commands as input and then executes them. This makes it easy for users unfamiliar with the terminal.

2. ### Advanced Commit Functionality
   We provide a functionality to automatically add most used commit messages. Simplifying the usage of git commit command
  
4. ### Squash Command
   We introduce the gits squash command that combines changes of last N commits and squash them into one. The number N can be provided using the -N argument, and the combined message for the commit is provided using the -M argument 
   
5. ### Advanced Visualisation Capabilities
   We introduce gits viz command that provides the git log functionality along with the feature that allows users to download a Directed Acyclic Graph Representation of the hierarchy of tags and branches 

## Potential Ideas for Phase 3

1. ### Enhancing the GUI to include advanced functionality 
   Contributors can think of enhancing the GUI implemented here to include branch information & commit history. They can also eschew the use of commands by introducing GUI elements to perform the functionality.

2. ### Suggestive command line interaction
   A good addition to the project would be to provide suggestive messages to the user when they enter a wrong or unintended command. This functionality can be extended to the oft misinterpreted/confusing commands.

3. ### Make the project more accessible by making GITS commands accessible to the local system.
   The lacunae that exists currently is that we need to clone the repository for each project to utilise GITS functionality. A feature that can be added is to make this global to the system where the repo is cloned. 


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


# Documentation
## Functionalities Implemented
These are the functionalities that we have implemented. The links are updated to point to the individual documentation.

1. [gits profile](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/profile.md)
2. [gits rebase](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/rebase.md)
3. [gits stash](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/stash.md)
4. [gits squash](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/squash.md)
5. [gits viz](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/viz.md)
6. [gits reset](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/reset.md)
7. [gits upstream](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/upstream.md)
8. [gits super reset](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/super_reset.md)
9. [gits commit](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/commit.md)
10. [gits create_branch](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/create_branch.md)
11. [gits logging](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/logging.md)
12. [gits undo](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/undo.md)
13. [gits untrack](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/untrack.md)
14. [gits track](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/track.md)
15. [gits delete](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/delete.md)
16. [gits sync](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/sync.md)
17. [gits switch](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/switch.md)
18. [gits status](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/status.md)
19. [gits branch](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/branch.md)
20. [gits diff](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/diff.md)
21. [gits init](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/init.md)
22. [gits merge](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/merge.md)
23. [gits push](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/push.md)
24. [gits pull](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/pull.md)



## Pydoc implementation
For easier access of Documentation use pydoc, run the following command, it will take you to a browser where you can view the documentation for all the files and directories.

`cd code`<br>
`python3 -m pydoc -b `


This repository is made for CSC 510 Software Engineering Course at NC State University.



### Use these Commands to harness the power of GITS
Use these commands to test GITS

- Create a test repo to test all the functionalities.
- Set the git profile name and email to "dummy_name" and "dummy@name.com" respectively. Once they are done,switch it back to the original ones.
- Create two branches with name: branch1 and branch2.
- Add some dummy text files to branch1. Commit these changes with an appropriate commit message.
- Switch to branch2 and add some text files to this branch.



### How to judge GITS??

1. Does this improve the way you work with git?? 
2. Did the process of creating a branch, committing, pushing changes and visualising the branch felt easier ??. 
3. Has the GUI made it easier for you to interact with your repo.??
4. Has advanced commit functionality helped you in committing efficiently?? Does this functionality make your commit history more intuitive and understanding


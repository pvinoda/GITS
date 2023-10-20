# About gits viz
gits viz provides the capability to visualise the commit history and branches. It combines the capabilities of git log and provides the extra feature to visualise the branches and commit history through a Directed Acyclic Graph (DAG). This graph will be stored in the configurations folder as a .png file

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/pvinoda/GITS/blob/master/code/gits_viz.py).

# Code Description
## Functions
1. gits_viz_func(args):
this function takes **args** object as an input. If arguments given include -g : download DAG, -s : simplified DAG output,-f : filename for the output.then the output will be generated and stored in configurations folder. Else git log will be run
# How to run it? (Small Example)
Lets say you want to visualise your branch structure and commit history, then you can run the below command
```
$ gits viz -g -s -f demo.png
```
If you just want to see the visualisation on the terminal, then run the below command
```
$ gits viz
```

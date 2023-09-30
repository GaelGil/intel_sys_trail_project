# intel_sys_trail_project


# Setup
There is no special setup required to run this project. You will just need the newest version of python to run the code

# About the project
In this project I implement the astar algoirhtm to find the optimal path between objectives. In the A* algorithm a very important topic is heuristics. In this project there are some heuristics we get to choose from to implement A*. We can choose a null heuristic (a heuristic value of 0), a manhattan distance heuristic, etc. As well as a heuristic value for multiple objectives. Additionally there are some pre genreated mazes however if you wish to generate a random maze you can do so as well.

To generate a maze simply do:
~~~python
python generate_maze.py
~~~

As mentioned we have some herustic values to choose from such as `null_heuristic`, `single_heuristic`, `better_heuristic`, `gen_heuristic`. To read more about them check the docstrings in `informed_search.py`

Lastly to run this project we can do: 

~~~python
python game.py new_maze.txt gen_heuristic
~~~



# Results
Below are some results using different heuristic values. 

~~~
python game.py new_maze.txt null_heuristic
Path length:  47
Carrots consumed:  335
Number of nodes expanded: 4,037
~~~

~~~
python game.py new_maze.txt single_heuristic
Path length:  47
Carrots consumed:  335
Number of nodes expanded: 3,873
~~~

~~~
python game.py new_maze.txt better_heuristic
Path length:  47
Carrots consumed:  335
Number of nodes expanded: 1,722
~~~


~~~
python game.py new_maze.txt gen_heuristic
Path length:  47
Carrots consumed:  335
Number of nodes expanded: 1,284
~~~
 
As we can see there we always get the same path length and number of carrots consumed which is to be expeted. However number of nodes expanded changes drastically. This goes to show that picking a good heuristic value can save us space and time. :)


import random


def generate_empty_maze(n):
    """
    Function to generate an empty maze.
    This is just a size nxn array of zeroes:
    param:
        n: an integer representing the size of array

    return: A array of size nxn
    """
    return [["-" for i in range(n)] for j in range(n)]

def generate_maze_structure(maze, num_obstacles, num_objectives):
   """
   Function to generate the strucute of a maze. This function will add 
   obstacles and objectives that the rover should go to.
   Param:
    maze: an empty nxn array
    num_obstacles: number of obstacles we want to have in the maze
    num_objectives: number of objectives the rover should stop at

   Return: A populated array with objectives and obstacles. 
   """
   structure = [random.sample(range(0, len(maze)), 2) for i in range(num_obstacles + num_objectives)]
   for i in range(len(structure)):
       if i < num_obstacles:
        x, y = structure[i]
        maze[x][y] = "W"
       else:
        x, y = structure[i]
        maze[x][y] = "M"
   return maze

def add_start(maze):
    """
    Function to add a starting point in the maze: This function simply iterates the maze and adds
    The starting point wherever is empty first. 
    Param:
        maze: The maze with obstacles and objectives
    Return: a maze with a start point
    """
    for i in range(len(maze)):
       for j in range(len(maze[i])):
          if maze[i][j] == "-":
             maze[i][j] = "S"
             return maze
    
def write_maze(maze, fname):
    """
    Function to wrtie the nxn array to a txt file.
    Param:
        maze: The complete maze with obstacles, objectives, and a start point.
        fname: The name of the file where we save the maze to.
    """
    f = open(fname, "a")
    for i in range(len(maze)):
       line = "".join(maze[i])
       f.write(f"{line}\n")
    f.close()

maze = add_start(generate_maze_structure(generate_empty_maze(15), 35, 5))
write_maze(maze, "./new_maze2.txt")

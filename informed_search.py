import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue() # pq for a*
    state = problem.start_state()
    root = data_structures.Node(state, None, None)
    fringe.push(root, heuristic(state, problem))
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.solution()  # we found a solution
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.expand(node.state):
                cost_to_child_node = node.cumulative_cost + action_cost # cost to a child node
                f = heuristic(child_state, problem) + (cost_to_child_node) # f(n) = h(n) + g(n) 
                child_node = data_structures.Node(child_state, node, action, cumulative_cost=cost_to_child_node) # save details into node
                if child_node not in fringe.heap or f < cost_to_child_node:
                    fringe.push(child_node, f) # add to fringe
    return None  # Failure -  no solution was found


def manhattan_distance(position, medal):
    """
    Returns the manhattan distance between two points
    :param
        position (tuple) representing the position of Sammy in the grid
        medal (tuple) representing the position of a given medal
    """
    pos_x, pos_y = position
    medal_x, medal_y = medal
    return (abs(pos_x-medal_x) + abs(pos_y-medal_y))


def carrots_to_medal(position, medal, problem):
    """
    Compute the number of carrots that  Sammy consumes to reach the
    given medal.
    :param
        position (tuple) representing the position of Sammy in the grid
        medal (tuple) representing the position of a given medal
        cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots consumed assuming Sammy
             does not take any unnecessary detours.
    """
    pos_x, pos_y = position
    medal_x, medal_y = medal
    x = abs(pos_x-medal_x)
    y = abs(pos_y-medal_y)
    res = [0]
    if pos_x > medal_x :
        res.extend([problem.cost[problem.WEST] for i in range(x)])
    else:
        res.extend([problem.cost[problem.EAST] for i in range(x)])
    if pos_y > medal_y:
        res.extend([problem.cost[problem.NORTH] for i in range(y)])
    else:
        res.extend([problem.cost[problem.SOUTH] for i in range(y)])
    return sum(res)


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*.
    Running A* with this null heuristic, gives us uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    A herustic value that is the manhattan distance between to points. Used
    for astar. This is heuristic will always be admisable because the
    heuristic will always be less than or equal to the actual distance
    travled. This function calls another function called manhattan_distance. 
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: an integer representing the manhatan distance between two points.
    """
    position, medals_left = state
    if problem.is_goal(state):
        return 0
    return manhattan_distance(position, medals_left[0])


def better_heuristic(state, problem):
    """
    A better heristic value constructed using the cost of a step in a certain direction.
    This heauristic will be admissible because 
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0 if goal state, if not then a heuristic value 
    """
    position, medals_left = state
    if problem.is_goal(state):
        return 0
    return carrots_to_medal(position, medals_left[0], problem)


def gen_heuristic(state, problem):
    """
    A heuristic value to use for astar when we have multiple medals on a map. This heuristic value
    will be admissible because it uses the same function that better_heuristic uses which we know
    is admissable. Additioanly we pick the max of those admissible heuristics. This will still give
    us an admissable heuristic. 
    :param
        state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
        problem: (a Problem object) representing the quest
    :return:
    """
    if problem.is_goal(state):
        return 0
    position, medals_left = state
    return max([carrots_to_medal(position, medal, problem) for medal in medals_left])


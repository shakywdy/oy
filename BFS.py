from collections import deque

############################
## Tree/Graph data structure
#############################

graph = {1: [2, 3], 2: [4, 5], 3: [6, 7]}
start_state = 1
goal_state = 5

##########################################
## Functions related to the problem domain
##########################################

def is_goal(x):
    return x == goal_state

##################
## Search Function
##################
def find_children(node):
    children = graph.get(node)
    if children:
        return children
    else:
        return []

def bfs_search(start_node):
    queue = deque()
    queue.append(start_node)
    visited = []
    end = False

    while queue and not end:
        next_node = queue.popleft()

        if next_node not in visited:
            print("Visiting node {} ".format(next_node))
            visited.append(next_node)
            if is_goal(next_node):
                print("Goal reached")
                end = True
            else:
                for child_node in find_children(next_node):
                    queue.append(child_node)

    if not end:
        print("Failed to find a goal state")


        
##################
## Main
##################
  

bfs_search(start_state)
input()

# wangdongyang s235458
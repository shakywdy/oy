
#Adding Path

############################
## Tree/Graph data structure
#############################

graph = {"A":["B","E"],       
         "B":["C","D"],  
           "D":["I","F"],
           "F":["G","H"],
           "H":["J","K"]

     


}

start_state = "A"
goal_state  = "K"

##########################################
## Functions related to the problem domain
##########################################

def is_goal(x):
    return x==goal_state
	
#############################################
# Functions for recording the Path
#
# A path is the states from the root to a certain goal node
# It is represented as a List of states from the root
# The create_path function create a new path by add one more node to an old path
##############################################

def create_path(old_path, new_state):
    new_path=old_path.copy()
    new_path.append(new_state)
    return new_path
    
##################
## Search Function
##################
def find_children(state):
    children = graph.get(state)
    if children:
        return children
    else:
        return []

def dfs_search(state):
    path = [state]
    next_node = (state, path) 
    visited = []
    to_visit = []
    

    end = False
    while not end: 
        next_state, path = next_node
        
        if not next_state in visited:
            print("Visiting node {} ".format(next_state))            
            visited.append(next_state)
            if is_goal(next_state):
                print("Goal reached!")
                end = True
                return path
            else:
                for child_state in find_children(next_state):
                    child_path = create_path(path, child_state)                    
                    to_visit.append([child_state, child_path])
			
        if to_visit:
            next_node=to_visit.pop()          
        elif not end:
            print("Failed to find a goal state")
            end=True
            return []


##################
## Main
##################


path = dfs_search(start_state)

if path: 
    print ("Path from start to goal: {}".format(path))
	
	
input()
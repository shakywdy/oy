#Name:YAN WAI KWOK
#student id:s235460



import copy



# Define the initial state and goal state
initial_state = {
    'left': {
        'people': 3,
        'barbarians': 3
    },
    'right': {
        'people': 0,
        'barbarians': 0
    },
    'boat': 'left'
}

goal_state = {
    'left': {
        'people': 0,
        'barbarians': 0
    },
    'right': {
        'people': 3,
        'barbarians': 3
    },
    'boat': 'right'
}

# Define the available moves
moves = [
    {'people': 1, 'barbarians': 0},  # Moving 1 person to the opposite side
    {'people': 0, 'barbarians': 1},  # Moving 1 barbarian to the opposite side
    {'people': 1, 'barbarians': 1},  # Moving 1 person and 1 barbarian to the opposite side
    {'people': 2, 'barbarians': 0},  # Moving 2 people to the opposite side
    {'people': 0, 'barbarians': 2},  # Moving 2 barbarians to the opposite side
]

# Verifies if the state is safe
def is_safe(state):
    if state['left']['people'] > 0 and state['left']['barbarians'] > state['left']['people']:
        return False
    if state['right']['people'] > 0 and state['right']['barbarians'] > state['right']['people']:
        return False
    return True

# Moves the people and barbarians to the opposite side
def move(what_to_move, old_state):
    new_state = copy.deepcopy(old_state)
    for key in what_to_move:
        new_state['left'][key] -= what_to_move[key]
        new_state['right'][key] += what_to_move[key]
    new_state['boat'] = 'right' if old_state['boat'] == 'left' else 'left'
    return new_state

# Generate child states
# Generate child states
def find_children(old_state):
    children = []
    for action in moves:
        new_state = move(action, old_state)
        if is_safe(new_state):
            # Check if the boat has at least one person or one barbarian
            if new_state['boat'] == 'left' and (new_state['left']['people'] >= 1 or new_state['left']['barbarians'] >= 1):
                children.append(new_state)
            elif new_state['boat'] == 'right' and (new_state['right']['people'] >= 1 or new_state['right']['barbarians'] >= 1):
                children.append(new_state)
    return children

# Depth-first search
def dfs_search(start_state):
    visited = []
    to_visit = []
    path = [start_state]
    next_state = start_state
    while True:
        if next_state not in visited:
            visited.append(next_state)
            if next_state == goal_state:
                print("Goal reached!")
                return path
            else:
                for child_state in find_children(next_state):
                    to_visit.append(child_state)
                    path.append(child_state)
        if to_visit:
            next_state = to_visit.pop()
        else:
            print("Failed to find a goal state")
            return []

# Search for a solution
path = dfs_search(initial_state)

if path:
    print("Path from start to goal:")
    for state in path:
        print(state)
else:
    print("No solution found.")

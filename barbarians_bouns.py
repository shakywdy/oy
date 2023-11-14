from collections import deque

# initial state
initial_state = {'left': {'people': 3, 'barbarians': 3}, 
                 'right': {'people': 0, 'barbarians': 0}, 
                 'boat': 'left'}

# goal state
goal_state = {'left': {'people': 0, 'barbarians': 0}, 
              'right': {'people': 3, 'barbarians': 3}, 
              'boat': 'right'}

moves = [
     # Move 1 person from left to right
    {'people': -1, 'barbarians': 0}, 
    # Move 1 barbarian from left to right
    {'people': 0, 'barbarians': -1},  
    # Move 1 person and 1 barbarian from left to right
    {'people': -1, 'barbarians': -1}, 
    # Move 2 people from left to right
    {'people': -2, 'barbarians': 0}, 
    # Move 2 barbarians from left to right 
    {'people': 0, 'barbarians': -2},  
]

def is_valid(state):
    if state['left']['people'] >= 0 and state['left']['barbarians'] >= 0 and state['right']['people'] >= 0 and state['right']['barbarians'] >= 0:
        if (state['left']['people'] == 0 or state['left']['people'] >= state['left']['barbarians']) and (state['right']['people'] == 0 or state['right']['people'] >= state['right']['barbarians']):
            return True
    return False

def find_children(state):
    children = []
    current_side = state['boat']
    opposite_side = 'left' if current_side == 'right' else 'right'
    for move in moves:
        child_state = {
            'left': {'people': state['left']['people'], 'barbarians': state['left']['barbarians']},
            'right': {'people': state['right']['people'], 'barbarians': state['right']['barbarians']},
            'boat': opposite_side
        }
        
        child_state[current_side]['people'] += move['people']
        child_state[current_side]['barbarians'] += move['barbarians']
        child_state[opposite_side]['people'] -= move['people']
        child_state[opposite_side]['barbarians'] -= move['barbarians']
        
        if is_valid(child_state):
            children.append(child_state)
    
    return children

def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal_state:
            return path
        
        visited.add(str(state))
        
        children = find_children(state)
        for child in children:
            if str(child) not in visited:
                queue.append((child, path + [child]))
    
    return None

solution = bfs(initial_state, goal_state)
if solution:
    print("Solution found!")
    for i, state in enumerate(solution):
        print(f"Step {i+1}: {state}")

    # wangdongyang s235458
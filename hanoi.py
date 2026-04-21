import copy

# Initialize rods
def initial_state(n):
    return {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

# Goal check
def is_goal(state, n):
    return state['C'] == list(range(n, 0, -1))

# Heuristic: number of disks on goal rod
def heuristic(state):
    return len(state['C'])

# Get all valid moves
def get_neighbors(state):
    rods = ['A', 'B', 'C']
    neighbors = []

    for src in rods:
        if not state[src]:
            continue
        for dest in rods:
            if src != dest:
                if not state[dest] or state[src][-1] < state[dest][-1]:
                    new_state = copy.deepcopy(state)
                    disk = new_state[src].pop()
                    new_state[dest].append(disk)
                    neighbors.append((new_state, f"{src} -> {dest}"))

    return neighbors

# Hill Climbing
def hill_climbing(n):
    current = initial_state(n)
    path = [current]

    while True:
        if is_goal(current, n):
            print("Goal reached!")
            return path

        neighbors = get_neighbors(current)

        # Choose best neighbor
        best = None
        best_h = heuristic(current)

        for state, move in neighbors:
            h = heuristic(state)
            if h > best_h:
                best = (state, move)
                best_h = h

        if best is None:
            print("Stuck in local optimum!")
            return path

        current, move = best
        path.append(current)

# Run
result = hill_climbing(3)

# Print steps
for step in result:
    print(step)
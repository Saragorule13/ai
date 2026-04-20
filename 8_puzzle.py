import heapq

# Goal state
goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

# Find position of a value in board
def find_pos(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

# Manhattan distance heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = find_pos(goal, val)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_pos(state, 0)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

# A* algorithm
def a_star(start):
    pq = [(heuristic(start), 0, start, [start])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            print("Steps to goal:", len(path)-1)
            for step in path:
                for row in step:
                    print(row)
                print()
            return

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

# Example start state
start = ((1,2,3),
         (4,0,6),
         (7,5,8))

a_star(start)
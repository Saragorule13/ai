graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, current, destination, visited, path):
    visited.add(current)
    path.append(current)

    if current == destination:
        print("DFS Path:", path)
        return True

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, destination, visited, path):
                return True

    path.pop()
    return False

# Call
visited = set()
dfs(graph, 'A', 'F', visited, [])





from collections import deque

def bfs(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == destination:
            print("BFS Path (Shortest):", path)
            return

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

# Call
bfs(graph, 'A', 'F')
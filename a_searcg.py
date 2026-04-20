import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (estimated cost to goal F)
heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

def a_star(graph, heuristic, start, goal):
    # (f, g, node, path)
    pq = [(heuristic[start], 0, start, [start])]
    visited = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Optimal Path:", path)
            print("Total Cost:", g)
            return

        if node in visited and visited[node] <= g:
            continue

        visited[node] = g

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

# Call
a_star(graph, heuristic, 'A', 'F')
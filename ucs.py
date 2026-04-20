import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(graph, start, goal):
    # priority queue: (cost, node, path)
    pq = [(0, start, [start])]
    visited = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        # If goal reached
        if node == goal:
            print("Optimal Path:", path)
            print("Total Cost:", cost)
            return

        # Avoid revisiting with higher cost
        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

# Call
ucs(graph, 'A', 'F')
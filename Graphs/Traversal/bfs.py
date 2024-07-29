from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    bfs_path = []

    while queue:
        vertex = queue.popleft()
        bfs_path.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_path


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs(graph, "A"))  # ['A', 'B', 'C', 'D', 'E', 'F']

def dfs(graph, vertex, dfs_path, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    dfs_path.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, dfs_path, visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

dfs_path = []
dfs(graph, "A", dfs_path)
print(dfs_path)  # ['A', 'B', 'D', 'E', 'F', 'C']

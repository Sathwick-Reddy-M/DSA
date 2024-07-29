from graph_utils import create_directed_graph_from_edges


def floyd_warshall(graph):
    n = len(graph)
    distances = [[float("infinity") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        distances[i][i] = 0

    for node in graph:
        for neighbor, weight in graph[node]:
            distances[node][neighbor] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )
    return distances


# Example graph
edges_with_negative_weights = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, -5),
    (1, 3, 10),
    (2, 4, 3),
    (4, 3, 4),
    (3, 5, 11),
]
graph = create_directed_graph_from_edges(edges_with_negative_weights)
# Run Floyd-Warshall algorithm
print(floyd_warshall(graph))

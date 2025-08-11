from Graphs.graph_utils import create_directed_graph_from_edges
from collections import defaultdict


def has_cycle_directed(graph):  # graph: dict[node] -> list[node]
    UNVISITED, VISITING, VISITED = 0, 1, 2

    color = defaultdict(int)  # default UNVISITED

    def dfs(u):
        color[u] = VISITING
        for v, _ in graph[u]:
            if color[v] == VISITING:
                return True
            if color[v] == UNVISITED and dfs(v):
                return True
        color[u] = VISITED
        return False

    for u in graph:
        if color[u] == UNVISITED and dfs(u):
            return True
    return False


directed_graph_with_cycle = create_directed_graph_from_edges(
    [
        (1, 2, 0),
        (2, 3, 0),
        (3, 1, 0),
        (3, 4, 0),
        (4, 5, 0),
        (5, 6, 0),
        (6, 4, 0),
    ]
)

print("Directed Graph with Cycle:", has_cycle_directed(directed_graph_with_cycle))

directed_graph_without_cycle = create_directed_graph_from_edges(
    [
        (1, 2, 0),
        (2, 3, 0),
        (3, 4, 0),
        (4, 5, 0),
        (5, 6, 0),
    ]
)

print(
    "Directed Graph without Cycle:",
    has_cycle_directed(directed_graph_without_cycle),
)

from Graphs.graph_utils import create_undirected_graph_from_edges


def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


undirected_graph_with_cycle = create_undirected_graph_from_edges(
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

print("Undirected Graph with Cycle:", has_cycle_undirected(undirected_graph_with_cycle))

undirected_graph_without_cycle = create_undirected_graph_from_edges(
    [
        (1, 2, 0),
        (2, 3, 0),
        (3, 4, 0),
        (4, 5, 0),
        (5, 6, 0),
    ]
)

print(
    "Undirected Graph without Cycle:",
    has_cycle_undirected(undirected_graph_without_cycle),
)

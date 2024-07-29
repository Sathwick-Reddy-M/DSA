def create_undirected_graph_from_edges(edges):
    graph = {}
    for edge in edges:
        node1, node2, weight = edge
        graph.setdefault(node1, []).append((node2, weight))
        graph.setdefault(node2, []).append((node1, weight))
    return graph


def create_directed_graph_from_edges(edges):
    graph = {}
    for edge in edges:
        node1, node2, weight = edge
        graph.setdefault(node1, []).append((node2, weight))
        graph.setdefault(node2, [])
    return graph

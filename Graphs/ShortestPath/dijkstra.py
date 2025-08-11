from Graphs.graph_utils import (
    create_undirected_graph_from_edges,
    create_directed_graph_from_edges,
)
import heapq


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance >= distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


# Example usage
edges = [("A", "B", 1), ("A", "C", 4), ("B", "C", 2), ("B", "D", 5), ("C", "D", 1)]

undirected_graph = create_undirected_graph_from_edges(edges)
directed_graph = create_directed_graph_from_edges(edges)

print("Undirected Graph:", undirected_graph)
print("Directed Graph:", directed_graph)

start_node = "A"
distances = dijkstra(undirected_graph, start_node)
print(f"Distances from start node {start_node} in undirected graph: {distances}")
# Output: Distances from start node A in undirected graph: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

distances = dijkstra(directed_graph, start_node)
print(f"Distances from start node {start_node} in directed graph: {distances}")
# Output: Distances from start node A in directed graph: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

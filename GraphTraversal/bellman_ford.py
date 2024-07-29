from collections import deque
from graph_utils import (
    create_undirected_graph_from_edges,
    create_directed_graph_from_edges,
)


def bellman_ford(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        updated = False
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    updated = True
        if not updated:
            break
    return distances


def bellman_ford_with_negative_cycle_detection(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        updated = False
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    updated = True
        if not updated:
            break

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = float("-infinity")
    return distances


# Shortest Path First Algorithm
# Function for Graphs with no negative cycles
def spfa(graph, start):
    n = len(graph)
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    queue = deque([start])
    update_count = {node: 0 for node in graph}

    while queue:
        current_node = queue.popleft()
        for neighbor, weight in graph[current_node]:
            if distances[neighbor] > distances[current_node] + weight:
                distances[neighbor] = distances[current_node] + weight
                update_count[neighbor] += 1
                if update_count[neighbor] > n:
                    return "Negative Cycle Detected"
                queue.append(neighbor)

    return distances


# Usage Examples
edges_with_negative_weights = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", -5),
    ("B", "D", 10),
    ("C", "E", 3),
    ("E", "D", 4),
    ("D", "F", 11),
]

directed_graph_with_negative_weights = create_directed_graph_from_edges(
    edges_with_negative_weights
)

print("Directed Graph with Negative Weights:", directed_graph_with_negative_weights)

start_node = "A"
distances = bellman_ford(directed_graph_with_negative_weights, start_node)
print(
    f"Distances from start node {start_node} in directed graph with negative weights using Bellman-Ford: {distances}"
)

distances_spfa = spfa(directed_graph_with_negative_weights, start_node)
print(
    f"Distances from start node {start_node} in directed graph with negative weights using SPFA: {distances_spfa}"
)

edges_with_negative_cycle = [("A", "B", 1), ("B", "C", 1), ("C", "A", -3)]
graph_with_negative_cycle = create_directed_graph_from_edges(edges_with_negative_cycle)

distances = bellman_ford_with_negative_cycle_detection(graph_with_negative_cycle, "A")
print(
    f"Distances from start node A in directed graph with negative cycle using Bellman-Ford with negative cycle detection: {distances}"
)

distances_spfa = spfa(graph_with_negative_cycle, "A")
print(
    f"Distances from start node A in directed graph with negative cycle using SPFA: {distances_spfa}"
)

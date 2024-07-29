# Shortest Path

## Just Curious

1. **What is the time complexity for brute force path finding?**

   The time complexity for brute force path finding is `O(V!)`, where `V` is the number of vertices (nodes) in the graph. This is because the brute force approach involves checking all possible permutations of the vertices to find the path, which results in factorial growth.

### Dijkstra's Algorithm

1. **Why is Dijkstra's algorithm so popular?**

   It efficiently finds the shortest path from a source node to all other nodes in a graph with non-negative edge weights. When using a basic approach like Bellman-Ford, which handles negative weights but has a time complexity of `O(V * E)`, or brute force methods with `O(V!)` complexity, Dijkstra's algorithm offers significant improvements. Using a priority queue (binary heap), it achieves a time complexity of `O((V + E) log V)`, and with a Fibonacci heap, it can be optimized to `O(E + V*log V)`.

2. **Why doesn't Dijkstra's algorithm work for negative edge weights?**

   Dijkstra's algorithm fails with negative edge weights because it assumes that once a node's shortest path is finalized, it won’t change. This assumption breaks if a shorter path is found later due to negative edge weights.

3. **If Dijkstra's algorithm is so famous and efficient, what about algorithms like A\*?**

   A\* uses heuristics to guide its search, making it more efficient than Dijkstra's algorithm in certain cases, especially when the goal is to find the shortest path between two specific nodes rather than from a single source to all nodes.

4. **Are there any algorithms that work for graphs with negative edge weights?**

   Yes, the Bellman-Ford algorithm is designed to handle graphs with negative edge weights. It can find the shortest path from a single source node to all other nodes, even in the presence of negative edge weights. Additionally, the Floyd-Warshall algorithm can handle negative edge weights and find shortest paths between all pairs of nodes, though it is less efficient for large graphs compared to Bellman-Ford.

5. **How do negative cycles affect shortest path calculations?**

   In the presence of a negative cycle, the concept of a "shortest path" becomes undefined, as continuously traversing the negative cycle can reduce the path length indefinitely. For example, in a graph with nodes A, B, and C and edges A → B with weight 1, B → C with weight -2, and C → A with weight -1, starting from A, the shortest path from A to C would initially be A → B → C with a weight of -1. However, repeatedly traversing the negative cycle C → A → B → C can reduce the path length further to arbitrarily negative.

6. **What about detecting negative cycles?**

   The Bellman-Ford algorithm can detect negative cycles by performing one additional iteration over all edges after the `V-1` iterations. If any distance can still be reduced, it indicates the presence of a negative cycle. The Floyd-Warshall algorithm can also detect negative cycles by checking if the distance from a node to itself becomes negative during the algorithm's execution or running the algorithm one additional iteration and checking if the optimial distance value still changes.

## Algorithms

## Time and Space Complexity

### Dijkstra's Algorithm

#### Time Complexity

The time complexity of Dijkstra's algorithm using a priority queue (min-heap) is `O((V + E) log V)`, where:

- `V` is the number of vertices (nodes) in the graph.
- `E` is the number of edges in the graph.

#### Space Complexity

The space complexity of Dijkstra's algorithm is `O(V + E)`, where:

- `V` is the number of vertices (nodes) in the graph.
- `E` is the number of edges in the graph.

This accounts for:

- The `distances` dictionary which stores the shortest distance to each node.
- The priority queue (min-heap) which can contain up to `E` elements in the worst case.

### Bellman-Ford Algorithm

#### Time Complexity

The time complexity of the Bellman-Ford algorithm is `O(V\*E)`, where:

- `V` is the number of vertices (nodes) in the graph.
- `E` is the number of edges in the graph.

This is because the algorithm performs `V - 1` iterations over all edges in the graph.

#### Space Complexity

The space complexity of the Bellman-Ford algorithm is `O(V)`, where:

- `V` is the number of vertices (nodes) in the graph.

This accounts for:

- The `distances` dictionary which stores the shortest distance to each node.

### Shortest Path Faster Algorithm (SPFA)

#### Time Complexity

The time complexity of the SPFA algorithm is `O(V*E)` in the worst case, where:

- `V` is the number of vertices (nodes) in the graph.
- `E` is the number of edges in the graph.

In the best case, the time complexity can be as good as `O(E)` if the graph is sparse and the shortest paths are found quickly.

#### Space Complexity

The space complexity of the SPFA algorithm is `O(V)`, where:

- `V` is the number of vertices (nodes) in the graph.

This accounts for:

- The `distances` dictionary which stores the shortest distance to each node.
- The `queue` which can contain up to `V` elements in the worst case.
- The `update_count` dictionary which tracks the number of updates for each node.

### Floyd-Warshall Algorithm

#### Time Complexity

The time complexity of the Floyd-Warshall algorithm is `O(V^3)`, where:

- `V` is the number of vertices (nodes) in the graph.

This is because the algorithm uses three nested loops, each running `V` times.

#### Space Complexity

The space complexity of the Floyd-Warshall algorithm is `O(V^2)`, where:

- `V` is the number of vertices (nodes) in the graph.

This accounts for:

- The `distances` matrix which stores the shortest distances between every pair of nodes.

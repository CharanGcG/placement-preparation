# Graph Representations in Python

This folder demonstrates various ways to represent graphs in Python, each suited for different types of problems and graph structures. Choosing the right representation can make algorithms more efficient and code easier to write.

---

## 1. Adjacency Matrix

- **Description:**  
  A 2D array where `matrix[i][j]` is `1` (or the weight) if there is an edge from node `i` to node `j`, else `0`.
- **Best for:**  
  Dense graphs, quick edge existence checks.
- **Space Complexity:**  
  O(V²), where V is the number of vertices.
- **Example:**
  ```python
  V = 4
  adj_matrix = [[0]*V for _ in range(V)]
  adj_matrix[0][1] = 1  # Edge from 0 to 1
  adj_matrix[1][2] = 1  # Edge from 1 to 2
  ```

---

## 2. Adjacency List

- **Description:**  
  A list (or dictionary) where each node stores a list of its neighbors.
- **Best for:**  
  Sparse graphs, efficient traversal.
- **Space Complexity:**  
  O(V + E), where E is the number of edges.
- **Example:**
  ```python
  adj_list = [[] for _ in range(V)]
  adj_list[0].append(1)
  adj_list[1].append(2)
  ```

---

## 3. Edge List

- **Description:**  
  A list of all edges, each represented as a tuple `(u, v)` or `(u, v, weight)`.
- **Best for:**  
  Algorithms that process edges directly (e.g., Kruskal's MST).
- **Space Complexity:**  
  O(E)
- **Example:**
  ```python
  edge_list = [(0, 1), (1, 2)]
  ```

---

## 4. Dictionary of Lists

- **Description:**  
  A dictionary where keys are node labels and values are lists of neighbors.
- **Best for:**  
  Graphs with non-integer or labeled nodes.
- **Example:**
  ```python
  graph_dict = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A'],
      'D': ['B']
  }
  ```

---

## 5. Weighted Graphs

- **Description:**  
  Adjacency lists or matrices can store weights for weighted graphs.
- **Example (Adjacency List with Weights):**
  ```python
  weighted_adj_list = [[] for _ in range(V)]
  weighted_adj_list[0].append((1, 5))  # Edge 0-1 with weight 5
  weighted_adj_list[1].append((2, 3))  # Edge 1-2 with weight 3
  ```

---

## 6. Using External Libraries

- **Description:**  
  Libraries like [NetworkX](https://networkx.org/) provide advanced graph data structures and algorithms.
- **Example:**
  ```python
  import networkx as nx
  G = nx.Graph()
  G.add_edge('A', 'B')
  G.add_edge('B', 'C')
  ```

---

## Summary Table

| Representation         | Space Complexity | Best For                | Notes                       |
|------------------------|------------------|-------------------------|-----------------------------|
| Adjacency Matrix       | O(V²)            | Dense graphs            | Fast edge checks            |
| Adjacency List         | O(V + E)         | Sparse graphs           | Efficient traversal         |
| Edge List              | O(E)             | Edge-centric algorithms | Simple structure            |
| Dictionary of Lists    | O(V + E)         | Labeled nodes           | Flexible node types         |
| Weighted Adjacency List| O(V + E)         | Weighted graphs         | Store weights with edges    |

---

## Tips

- Use adjacency lists for most competitive programming problems (unless the graph is very dense).
- Adjacency matrices are useful for algorithms that require frequent edge existence checks.
- Edge lists are ideal for algorithms like Kruskal's Minimum Spanning Tree.
- For labeled graphs, dictionaries provide flexibility.
- For advanced use cases, consider libraries like NetworkX.

---

## Further Reading

- [GeeksforGeeks: Graph and its representations](https://www.geeksforgeeks.org/graph-and-its-representations/)
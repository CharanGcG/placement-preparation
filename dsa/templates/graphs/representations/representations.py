# Graph Representations in Python

# 1. Adjacency Matrix
# Suitable for dense graphs. Space: O(V^2)
V = 4
adj_matrix = [[0]*V for _ in range(V)]
# Example: Add edge 0-1 and 1-2
adj_matrix[0][1] = 1
adj_matrix[1][2] = 1

# 2. Adjacency List
# Suitable for sparse graphs. Space: O(V + E)
adj_list = [[] for _ in range(V)]
# Example: Add edge 0-1 and 1-2
adj_list[0].append(1)
adj_list[1].append(2)

# 3. Edge List
# List of all edges. Useful for algorithms like Kruskal's.
edge_list = []
# Example: Add edge 0-1 and 1-2
edge_list.append((0, 1))
edge_list.append((1, 2))

# 4. Dictionary of Lists (for labeled nodes)
# Useful when nodes are not integers.
graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

# 5. Weighted Graphs
# Adjacency list with weights
weighted_adj_list = [[] for _ in range(V)]
# Example: Add edge 0-1 with weight 5, 1-2 with weight 3
weighted_adj_list[0].append((1, 5))
weighted_adj_list[1].append((2, 3))

# Print examples
print("Adjacency Matrix:", adj_matrix)
print("Adjacency List:", adj_list)
print("Edge List:", edge_list)
print("Dictionary of Lists:", graph_dict)
print("Weighted Adjacency List:", weighted_adj_list)
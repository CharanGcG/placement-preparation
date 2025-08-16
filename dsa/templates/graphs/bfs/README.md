# Breadth-First Search (BFS) in Graphs

This folder demonstrates how to implement Breadth-First Search (BFS) for different graph representations in Python. BFS is a fundamental graph traversal algorithm used to explore nodes level by level, making it useful for finding shortest paths in unweighted graphs, checking connectivity, and more.

---

## What is BFS?

- **BFS** explores all neighbors of a node before moving to the next level.
- It uses a **queue** to keep track of nodes to visit.
- BFS guarantees the shortest path in unweighted graphs.

---

## BFS Algorithm Steps

1. Start from the source node.
2. Mark the source as visited and enqueue it.
3. While the queue is not empty:
   - Dequeue a node.
   - Visit all its unvisited neighbors, mark them as visited, and enqueue them.

---

## BFS Implementations

### 1. BFS for Adjacency Matrix

```python
def bfs_adj_matrix(matrix, start):
    V = len(matrix)
    visited = [False] * V
    queue = deque([start])
    visited[start] = True
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in range(V):
            if matrix[node][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order
```

### 2. BFS for Adjacency List

```python
def bfs_adj_list(adj_list, start):
    V = len(adj_list)
    visited = [False] * V
    queue = deque([start])
    visited[start] = True
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order
```

### 3. BFS for Edge List

```python
def bfs_edge_list(edge_list, start, V):
    from collections import defaultdict
    adj_list = defaultdict(list)
    for u, v in edge_list:
        adj_list[u].append(v)
        adj_list[v].append(u)  # For undirected graph
    visited = [False] * V
    queue = deque([start])
    visited[start] = True
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order
```

### 4. BFS for Dictionary of Lists (Labeled Nodes)

```python
def bfs_dict(graph_dict, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph_dict.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

### 5. BFS for Weighted Adjacency List (Ignoring Weights)

```python
def bfs_weighted_adj_list(weighted_adj_list, start):
    V = len(weighted_adj_list)
    visited = [False] * V
    queue = deque([start])
    visited[start] = True
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor, _ in weighted_adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order
```

---

## Applications of BFS

- Finding shortest path in unweighted graphs
- Checking graph connectivity
- Level order traversal in trees
- Cycle detection in undirected graphs
- Solving puzzles (e.g., shortest moves in chess)

---

## Tips

- Always mark nodes as visited when enqueuing to avoid revisiting.
- BFS is ideal for problems requiring minimal steps or levels.
- For weighted graphs, use Dijkstra’s algorithm instead.

---

## Further Reading

- [GeeksforGeeks: Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [LeetCode Graph BFS Problems](https://leetcode.com/tag/breadth-first-search/)
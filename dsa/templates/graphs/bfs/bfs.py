from collections import deque

# 1. BFS for Adjacency Matrix
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

# 2. BFS for Adjacency List
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

# 3. BFS for Edge List
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

# 4. BFS for Dictionary of Lists (labeled nodes)
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

# 5. BFS for Weighted Adjacency List (ignores weights for traversal)
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
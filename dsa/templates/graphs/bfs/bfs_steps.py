def bfs_adj_list(start, adj_list, n, step_cost=6):
    queue = [(start, 0)]
    visited = set()
    visited.add(start)
    bfs = [-1] * n
    bfs[start] = 0
    while queue:
        node, cost = queue.pop(0)
        bfs[node] = cost
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append((neighbor, cost + step_cost))
                visited.add(neighbor)
    return bfs
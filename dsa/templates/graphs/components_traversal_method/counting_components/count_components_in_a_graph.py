def count_components(graph):
    """
    Counts the number of connected components in an undirected graph using BFS.
    Can be extended to handle directed graphs by modifying the adjacency representation.
    """
    visited = set()
    def bfs(start):
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            for neighbor in range(len(graph)):
                if neighbor not in visited and graph[node][neighbor]==1:
                    queue.append(neighbor)
                    visited.add(neighbor)
    
    components = 0

    for node in range(len(graph)):
        if node not in visited:
            components += 1
            bfs(node)
    return components
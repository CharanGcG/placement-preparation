from collections import defaultdict

def get_adj_list_and_indegree(n, edges):
    adj_list = defaultdict(list)
    indegree = [0] * n
    for dest, source in edges:
        adj_list[source].append(dest)
        indegree[dest] += 1
    return adj_list, indegree


def topological_sort(n, edges):
    adj_list, indegree = get_adj_list_and_indegree(n, edges)
    queue = [i for i in range(n) if indegree[i] == 0]
    topological_order = []
    if not queue:
        return False
    while queue:
        node = queue.pop(0)
        topological_order.append(node)
        for neighbor in adj_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(topological_order) < n:
        return False
    return True
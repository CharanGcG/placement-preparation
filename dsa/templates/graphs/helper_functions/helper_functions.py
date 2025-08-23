from collections import defaultdict

def edges_to_adj_list(edges):
    """
    Convert a list of edges to an adjacency list representation.    
    """
    adj_list = defaultdict(list)
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def adj_matrix_to_adj_list(adj_matrix):
    """
    Convert an adjacency matrix to an adjacency list representation.
    """
    adj_list = defaultdict(list)
    n = len(adj_matrix)
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list
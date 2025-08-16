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
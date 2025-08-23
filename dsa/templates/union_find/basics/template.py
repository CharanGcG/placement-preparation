def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union_by_rank(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x == root_y:
        return
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_y] > rank[root_x]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    return

def union_by_size(x, y, parent, size):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x == root_y:
        return
    if size[root_x] > size[root_y]:
        parent[root_y] = root_x
        size[root_x] += size[root_y]
    else:
        parent[root_x] = root_y
        size[root_y] += size[root_x]
    return

def count_components(parent):
    roots = set()
    for i in range(len(parent)):
        roots.add(find(i, parent))
    return len(roots)

n = 10 # Number of elements
parent = [i for i in range(n)]
rank = [0] * n
size = [1] * n
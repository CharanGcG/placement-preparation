# Topological Sort: Documentation for README

## Overview

**Topological Sort** is a fundamental algorithm in graph theory used to order the vertices of a **directed, acyclic graph (DAG)** such that for every directed edge `uv` from vertex `u` to vertex `v`, `u` comes before `v` in the ordering. It's widely used in scenarios involving dependencies—such as course schedules, task ordering, build systems, etc.[1]

***

## When to Use Topological Sort

- **Dependency resolution:** When tasks depend on the completion of other tasks.
- **Directed graphs:** Works only on directed graphs.
- **Cycle detection:** Checks whether cycles exist in the dependency graph.
- **Examples:** Course prerequisite scheduling, task automation, build systems (e.g., Makefile), event dependencies, data transformation pipelines.

***

## Data Structures Required

1. **Adjacency List:** List where each vertex’s outgoing edges are stored.
2. **Indegree Array:** Array tracking the number of incoming edges for every vertex.
3. **Queue:** Used to process vertices with zero indegree (independent tasks).

***

## Basic Idea

Sort elements in the order in which their prerequisites are satisfied. The vertices are processed such that all dependencies are resolved before a task begins.

***

## Example

Suppose we want to complete a set of courses, but some courses depend on others:

- Prerequisite list:
    - `prerequisite[i][j] = [a_i, b_i]`
    - To take course `a_i`, you must complete course `b_i` first.

Adjacency List Example:
- Course 0 is a prerequisite for courses 1, 2, and 3.
- Courses 1, 2, and 3 can only be taken after completing course 0.

***

## Algorithm (Kahn’s Algorithm - BFS Approach)

1. **Build adjacency list and indegree array for all vertices.**
2. **Enqueue all vertices with indegree zero (no dependencies).**
3. **Process queue:**
    - Pop vertex from queue, add to the topological order.
    - For each neighbor, decrement its indegree.
    - If a neighbor’s indegree becomes zero, enqueue it.
4. **Repeat until the queue is empty.**

If the number of processed vertices equals the total number of vertices, no cycle exists (valid order found). Otherwise, the graph contains a cycle (not possible to resolve all dependencies).

***

## Pseudocode

```python
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
```

***

## Usage Example

Suppose you have `n` tasks with dependencies represented as edges.

- Input: `n = 4`, edges = `[, , ]`[1]
- Output: `` (or any permutation where 0 comes before 1, 2, 3)[1]

***

## Cycle Detection

If the size of the topological order is **not equal** to number of vertices, the graph contains a cycle (no valid scheduling is possible).

***

## Real-World Analogy

Think of enrolling in university courses:
- You can’t take **Advanced Algorithms** before completing **Basic Algorithms**.
- The university system sorts all your courses across semesters applying topological sort.

***

## Reference

This documentation is designed based on structured logical notes and practical examples, providing a concise, actionable summary for technical interviews and quick revision needs.[1]

[1]

***

**Interview Tip:** In coding rounds, always check for cycles and handle cases where not all tasks can be scheduled due to impossible dependencies (cycles).

**Key term:** “Directed Acyclic Graph (DAG)”—topological sort only works for DAGs.

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/95182679/56b8b380-0926-4466-852a-59ee7f47a014/WhatsApp-Image-2025-08-23-at-15.39.25_b13c119f.jpg?AWSAccessKeyId=ASIA2F3EMEYE53IDCNEI&Signature=gGDkKl49Se6xwsWl8c4CEf0mmm0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIBU7C%2BOhOtZ2MRWrjbt2FaPxvJ8VxJoFJdabKxuUzYUEAiAfqRuDvgRFM%2FSBlidhpbXWxTb%2BggGcWOkZACZNNrA%2BqSrxBAgrEAEaDDY5OTc1MzMwOTcwNSIMJICmSG%2BLmJC8iBCGKs4EfkwPMTnQ20wg%2FWCvQjmOr%2Fm8GROzPQ2qga7mv5BNdtHqgDyxdqn577LAS3%2F6mpMa1EH9Qa26OmUgP81ecPF8DaqbTPGkSFVrklsmx%2BUg%2BzP0qyr%2FSlSlZahOen4r5q6IbpotBQIzgb2owlat6XCLffIAMNdhDc1NlC1%2B8qh1TJ6CFi1aq%2FwhUUwt3bHlaXwl7ZlMh7Cyx%2FOeKiRg8B%2BzDcxZyw1sSU4MudSwiuM85oU4pn2TBDVVpG2dm0MWAWKI3KMhaBUChaTe162dOL6Pxwf7lwbgXFuRUXmw176zM58db5KqE%2FfPq5zswyehmk44bzC4tgNWsCFMAz4mRqArIQ2AR9tLgiQDA%2FC8TWOrO9Pe37BvtVwdSAaLmKnckOaXxtvzQMisuq5s5JnNBXmYHplTExhpFizZj6gxUqsjY4MmUP2sokgFYMc2igPG0F0hVClbSasMK73qxXkYJJ%2BUnMOIXyBOJitjP4UUahVpbbJrilbLwP8nv7A3kUjZXQhw3iEsylOMRCZEhLegEt%2FOp5FMmoH%2FCm9y7SfGcnCsUlp5d6FcA9vZj8%2F5AR7Nh6XEkV2gIH7Bql2j%2BNJ%2BN3Ey1RLVoXqoKa4cBj7Q%2F3xylEp3Wcl6%2B05PtUt38%2FYETc62E%2BPyttgnFkZmBK7g0Asc8zUslyndw1g5aL1k1Xmajs2rqcbMSpmGzWAhrBAadwb%2Fcl29nITStHQkklxmxpUkXk1Ruw%2B56FXbINtDsqYFlMTGisa%2BwT%2FxaNZ7QoyUIo7AyHx22nOMbDgGWFWIS%2FkwhJamxQY6mwGeTm36Mmsrr6XqNLN4PTBnHaIxxjDKXEOI1bsuHPb2Ag40XKBzO%2FZwked7HkKWqgfIIk2n2VGNYC6LUfWdvH72yParLIeHMR4PNQ%2FAMGlVgWvXUCljYZaBpcJ1gdEmqUybvmfBA5k0aGe9B2Zgko6SgnbA4w51drRANepsOv1IkE0iBaJbPMisvaRPpryGtSfSEJmFlXhlM%2Fxmmw%3D%3D&Expires=1755944451)
# Connected Components: Quick Recognition & Action Guide

Recognizing when a problem is about **connected components** is a crucial skill in coding rounds. This guide helps you quickly spot such problems and solve them efficiently.

---

## 🚨 Mental Detector: When is it a Connected Components Problem?

### 1. **Input Format Signals**
- Edge lists: `from[]`, `to[]`
- Node/edge counts: `n` nodes, `m` edges, followed by pairs
- Matrix/grid: Each cell is a node, edges to neighbors

**Rule:** If you see entities + relations/pairs → think graph.

---

### 2. **Keyword Clues**
Look for words like:
- “How many groups?”
- “Isolated sets”
- “Clusters”
- “Pairs from different groups”
- “Minimum resources per group”

---

### 3. **Classic Examples**
- Roads and Libraries (Hackerrank)
- Journey to the Moon (Hackerrank)
- Number of Provinces (LeetCode 547)
- Friend Circles
- Island Problems (LeetCode 200, 695)

---

## 🧭 Decision Flowchart

```
Entities + Relations? → Build Graph
         |
         v
Ask about groups/clusters? → Connected Components
         |
         v
Min resources per group? → 1 per component
         |
         v
Pairs between groups? → Use component sizes
```

---

## ⚡ Fast Action Plan

1. **Build adjacency list** from input.
2. **Run BFS/DFS** to find components.
3. **Store component sizes** if needed.
4. **Apply problem-specific logic**.

---



## 💡 Rule of Thumb
If “not everyone is directly connected but can reach indirectly,” you’re in connected components land!


---
# 📘 Problem Documentation: **Minimum Subset Cost Partitioning**

### **Problem Statement**

Given an array `arr[]`, split it into **subsets of size ≥ 3**.
The **cost of a subset** is defined as:

$$
\text{cost(subset)} = \max(subset) - \min(subset)
$$

Your task is to partition the array into valid subsets such that the **total cost** (sum of subset costs) is minimized.

Return the **minimum possible total cost**.

---

### **Example Test Cases**

#### Example 1:

```
Input: arr = [1, 2, 3, 10, 11, 12]
Output: 2
```

**Explanation:**
Possible split:

* Subset 1: \[1, 2, 3] → cost = 3 - 1 = 2
* Subset 2: \[10, 11, 12] → cost = 12 - 10 = 2
  Total = 2 + 2 = 4

But if we sort and consider grouping better:

* Subset: \[1, 2, 3, 10, 11, 12] → cost = 12 - 1 = 11 (worse).

✅ Best partition = \[1,2,3] and \[10,11,12], min cost = **4**

---

#### Example 2:

```
Input: arr = [5, 1, 9, 2, 6, 3]
Output: 4
```

**Explanation:**
Sort: \[1,2,3,5,6,9]

* Subset 1: \[1,2,3] → cost = 2
* Subset 2: \[5,6,9] → cost = 4
  Total = 6

But if we group \[1,2,3,5,6] and \[9]: invalid (second subset < 3).

✅ Best cost = **6**

---

#### Example 3:

```
Input: arr = [4, 8, 10, 7, 9, 6]
Output: 4
```

**Explanation:**
Sort: \[4,6,7,8,9,10]

* Subset 1: \[4,6,7] → cost = 3
* Subset 2: \[8,9,10] → cost = 2
  Total = 5

✅ Minimum = 5

---

---

### **Approach to Solve**

1. **Sorting First**
   Since cost depends only on min and max, **sorting ensures grouping close numbers minimizes cost**.

2. **Dynamic Programming (DP)**
   Define `dp[i]` = minimum cost to split first `i` elements.
   Transition:

   ```
   dp[i] = min( dp[j] + (arr[i] - arr[j+1]) )  
   for all j <= i-3
   ```

   because each subset must have at least size 3.
   Base case: `dp[0] = 0`.

   Final answer: `dp[n]`.

3. **Greedy Won’t Work**
   A naive greedy grouping of consecutive triplets may fail (sometimes making one group larger reduces cost).

---

### **Solution (Python)**

```python
def minSubsetCost(arr):
    arr.sort()
    n = len(arr)
    INF = float('inf')
    
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(3, n + 1):  # groups of at least size 3
        for j in range(i - 3, -1, -1):
            cost = arr[i-1] - arr[j]
            dp[i] = min(dp[i], dp[j] + cost)
    
    return dp[n]

# Example Runs
print(minSubsetCost([1, 2, 3, 10, 11, 12]))  # 4
print(minSubsetCost([5, 1, 9, 2, 6, 3]))     # 6
print(minSubsetCost([4, 8, 10, 7, 9, 6]))    # 5
```

---

### **Related Questions**

* Split array into **k subsets** minimizing/maximizing cost.
* Minimum cost partition with **different subset size constraints**.
* Similar DP patterns:

  * “Partition array into subarrays of size ≤ k with min/max cost”
  * “Minimize difference between groups”
  * LeetCode style: *Partition Array for Minimum Sum Difference*.

---

### **How to Face in Future**

✅ Recognize **keywords**: “split/partition” + “minimize/maximize cost” ⇒ almost always **DP**.
✅ First step: **sort** if problem involves min/max.
✅ Think: **can greedy fail?** If yes, try DP.
✅ Write down small test cases and manually try groupings to see the pattern.
✅ In assessments, focus on **correct approach over code optimization** (but if stuck, mention DP idea).



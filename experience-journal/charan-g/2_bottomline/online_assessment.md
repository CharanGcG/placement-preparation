
# 📘 Problem Documentation: **House Relocation by Language Grouping**

### **Problem Statement**

We are given an array where:

* Each index represents a **house**.
* Each element represents the **language** spoken in that house (an integer).
* Maximum language value is **K** (languages are `1..K`).

The **goal** is to relocate houses so that people who speak the **same language are grouped together**.
Allowed operation:

* A house at index `i` can be swapped **only with its immediate neighbor** (`i-1` or `i+1`).

We must compute the **minimum number of swaps** required to reach the most optimal arrangement.

---

### **Example Test Cases**

#### Example 1

```
Input:  [1, 2, 1, 2]
Output: 1
```

**Explanation:**

* If we swap index `1 (value=2)` with index `2 (value=1)`, we get `[1, 1, 2, 2]`.
* Only **1 swap** is needed.

---

#### Example 2

```
Input:  [3, 1, 3, 2, 2, 1]
Output: 4
```

**Explanation:**
One optimal arrangement is `[1, 1, 2, 2, 3, 3]`.
The minimum swaps required to cluster same-language houses = **4**.

---

#### Example 3

```
Input:  [1, 2, 3, 1, 2, 3]
Output: 6
```

**Explanation:**
Final arrangement could be `[1, 1, 2, 2, 3, 3]`.
To bring same languages together, at least **6 swaps** are required.

---

---

### **Approach to Consider**

1. **Observation**

   * This problem is about **minimum adjacent swaps to cluster identical elements**.
   * The key difficulty is that we can only swap with neighbors.

2. **Core Idea**

   * For each language group, their final position must be a **contiguous block**.
   * To minimize swaps, we want to bring all instances of a language close to their **median position**.
   * This is similar to the "minimum adjacent swaps to make elements consecutive" problem.

3. **Steps**

   * Collect all indices of each language.
   * For each language `L`:

     * Suppose its positions are `[i1, i2, i3, …, im]`.
     * Find the **median index** `mid`.
     * Target positions will be `[t, t+1, t+2, …, t+m-1]` centered around `mid`.
     * Number of swaps = `Σ |ij - (t + j)|`.
   * Add this for all languages.
   * Return the total minimum swaps.

---

### **Solution (High-Level Pseudocode)**

```python
def min_swaps(arr):
    from collections import defaultdict
    
    # Step 1: Collect positions of each language
    positions = defaultdict(list)
    for i, val in enumerate(arr):
        positions[val].append(i)
    
    swaps = 0
    
    # Step 2: For each language group
    for lang, idxs in positions.items():
        m = len(idxs)
        # Median-based alignment
        median = idxs[m // 2]
        
        # Target positions: [median - m//2 ... median + m//2]
        for j in range(m):
            swaps += abs(idxs[j] - (median - m//2 + j))
    
    return swaps
```

---

### **Complexity**

* Time: **O(N)** (since we just collect indices and compute differences).
* Space: **O(N)** (storing positions).

---

### **Related Questions**

* Minimum adjacent swaps to make a string palindrome.
* Minimum swaps to sort an array.
* Minimum swaps to group all 1s together.
* Grouping people by attributes with minimal cost.

---

### **How to Face Similar Questions in Future**

1. **Look for “grouping” or “clustering” patterns** → Think about median alignment.
2. **Remember adjacent swaps = distance between current index and target index.**
3. **Break problem into groups** (one language at a time, one character at a time).
4. **Try greedy median approach** instead of brute force.
5. **Practice related swap problems** so spotting the pattern becomes natural.



---


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



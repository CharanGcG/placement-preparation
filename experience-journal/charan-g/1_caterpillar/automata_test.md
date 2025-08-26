
# 📘 Problem Documentation: **Find the Town Name from Residents' Names**

---

### **Problem Statement**

You are given an array of names of people from a town.
In this town, **every resident’s name starts with the town name as a prefix** (case-insensitive).

Return the **town name in lowercase**.

---

### **Example Test Cases**

#### Example 1

```
Input:  ["HydCharan", "HydRamesh", "hydAnita"]
Output: "hyd"
```

**Explanation:**

* All names start with `"hyd"` (case-insensitive).
* Return `"hyd"`.

---

#### Example 2

```
Input:  ["BangaloreRaj", "bangaloreSneha", "BANGALORESunil"]
Output: "bangalore"
```

**Explanation:**

* Common prefix (ignoring case) = `"bangalore"`.
* Answer = `"bangalore"`.

---

#### Example 3

```
Input:  ["Delhishyam", "Delhiajay", "DelhiNisha"]
Output: "delhi"
```

---

#### Example 4 (Edge Case)

```
Input: ["Chennai", "CHENnailakshmi", "chennaiarun"]
Output: "chennai"
```

---

---

### **Approach to Consider**

1. **Normalize Case**

   * Convert all names to lowercase (since comparison must be case-insensitive).

2. **Find the Longest Common Prefix (LCP)**

   * This is a **classic string problem** → we need the **common prefix of all strings**.
   * Apply the standard **Longest Common Prefix** approach.

3. **Steps**

   * Convert all names to lowercase.
   * Pick the first string as a reference.
   * Compare character by character with other strings.
   * Stop when mismatch occurs.
   * The resulting prefix is the **town name**.

---

### **Solution (Python)**

```python
def findTownName(names):
    # Step 1: Normalize
    names = [name.lower() for name in names]
    
    # Step 2: Start with first string as prefix
    prefix = names[0]
    
    # Step 3: Check prefix with each name
    for name in names[1:]:
        # shrink prefix until it matches
        while not name.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix
```

---

### **Complexity**

* Time: **O(N \* L)**, where `N` = number of names, `L` = average length of names.
* Space: **O(1)** (ignoring input).

---

### **Related Questions**

* Longest Common Prefix (LeetCode #14).
* Find common prefix/suffix in a set of strings.
* String normalization problems (case-insensitive comparisons).
* Detect company name prefix from employee emails/usernames.

---

### **How to Face Similar Questions in Future**

1. **Notice “prefix” pattern** immediately → it’s often a longest common prefix problem.
2. **Don’t forget normalization** (case-insensitive often hidden in wording).
3. **Always test edge cases**:

   * All names identical.
   * Only one name.
   * No common prefix (if allowed, answer = "").
4. **Practice string prefix/suffix problems** since they are frequent in online assessments.





# 📘 Problem Documentation: **Find the Kth Largest Element**

---

### **Problem Statement**

Given an array of integers `arr[]` of size `n` and a value `k`, return the **kth largest element** in the array.

* Largest means in **descending order** (1st largest = maximum).
* It is **not** asking for distinct elements (so duplicates count separately unless specified).

---

### **Example Test Cases**

#### Example 1

```
Input:  arr = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Explanation:**
Sorted in descending order → \[6, 5, 4, 3, 2, 1]
2nd largest = **5**

---

#### Example 2

```
Input:  arr = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Explanation:**
Sorted → \[6, 5, 5, 4, 3, 3, 2, 2, 1]
4th largest = **4**

---

#### Example 3

```
Input:  arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 10
```

**Explanation:**
Sorted → \[20, 15, 10, 7, 4, 3]
3rd largest = **10**

---

---

### **Approaches to Consider**

1. **Sorting (Naive)**

   * Sort array in descending order.
   * Return `arr[k-1]`.
   * **Time:** O(n log n)
   * **Space:** O(1)
   * Works fine for small constraints.

---

2. **Heap (Efficient)**

   * Use a **min-heap** of size `k`.
   * Traverse array:

     * Push element to heap.
     * If heap size > k → pop smallest.
   * At the end, heap root = kth largest.
   * **Time:** O(n log k)
   * **Space:** O(k)
   * Best choice for large arrays.

---

3. **Quickselect (Optimal Average)**

   * Use **Quickselect algorithm** (variation of Quicksort partitioning).
   * Partition the array until pivot = kth largest.
   * **Time:** O(n) average, O(n²) worst-case.
   * **Space:** O(1).
   * Often used in competitive coding / interviews.

---

---

### **Solution (Python — Heap Approach)**

```python
import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

---

### **Solution (Python — Quickselect Approach)**

```python
import random

def partition(nums, left, right, pivot_index):
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] > pivot:  # greater first (descending)
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index

def quickselect(nums, left, right, k):
    if left <= right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(nums, left, right, pivot_index)
        
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            return quickselect(nums, pivot_index+1, right, k)
        else:
            return quickselect(nums, left, pivot_index-1, k)

def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums)-1, k-1)
```

---

### **Complexity Comparison**

| Approach    | Time Complexity | Space Complexity | Notes                                |
| ----------- | --------------- | ---------------- | ------------------------------------ |
| Sorting     | O(n log n)      | O(1)             | Easiest, but not optimal             |
| Heap        | O(n log k)      | O(k)             | Best for streaming/large n           |
| Quickselect | O(n) avg        | O(1)             | Best in practice if implemented well |

---

### **Related Questions**

* Find the **kth smallest** element.
* Find the **median** of an unsorted array.
* Find **top K frequent elements**.
* Find **top K largest elements in a stream**.
* “Order statistics” problems in general.

---

### **How to Face Similar Questions in Future**

1. **Clarify if duplicates matter** (are we finding kth distinct or kth with duplicates?).
2. **Choose approach based on input size:**

   * Small arrays → Sorting.
   * Large arrays / online stream → Heap.
   * Competitive coding → Quickselect.
3. **Remember:**

   * Heap gives a running `kth largest`.
   * Quickselect is like a "smart search" without full sorting.
4. **Practice related selection problems** — once you master kth largest, you’ll quickly spot when to apply heap or quickselect in other questions.

---

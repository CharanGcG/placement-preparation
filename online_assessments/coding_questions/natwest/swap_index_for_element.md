# 📘 Problem Documentation: **Swap Index with Value (Inverse Mapping of Array)**

---

### **Problem Statement**

We are given an array `arr` of size `n`, where:

* Each element is **unique**.
* Elements are integers within the range `[0, n-1]`.

We need to **transform the array** such that:

* If `arr[i] = j`, then in the new array, `arr[j] = i`.

This essentially means we are computing the **inverse mapping** of the array.

---

### **Example Test Cases**

#### Example 1

```
Input:  [2, 0, 1]
Output: [1, 2, 0]
```

**Explanation:**

* arr\[0] = 2 → so new\[2] = 0
* arr\[1] = 0 → so new\[0] = 1
* arr\[2] = 1 → so new\[1] = 2

---

#### Example 2

```
Input:  [3, 0, 2, 1]
Output: [1, 3, 2, 0]
```

**Explanation:**

* arr\[0] = 3 → new\[3] = 0
* arr\[1] = 0 → new\[0] = 1
* arr\[2] = 2 → new\[2] = 2
* arr\[3] = 1 → new\[1] = 3

---

#### Example 3

```
Input:  [4, 0, 2, 1, 3]
Output: [1, 3, 2, 4, 0]
```

---

---

### **Approach to Consider**

1. **Direct Construction (Extra Array)**

   * Create a new array `res` of size `n`.
   * Traverse input array: for each index `i`, place `i` at position `arr[i]` in `res`.
   * Return `res`.
   * **Time:** O(n), **Space:** O(n).

2. **In-Place Approach (Tricky)**

   * Modify array without extra space by encoding values.
   * But since question is for online assessments, extra array approach is cleaner and less error-prone.

---

### **Solution (Python — Extra Array)**

```python
def inverse_array(arr):
    n = len(arr)
    res = [0] * n
    for i in range(n):
        res[arr[i]] = i
    return res
```

---

### **Complexity**

* Time: **O(n)**
* Space: **O(n)** (for result array; in-place is possible but tricky and unnecessary here).

---

### **Related Questions**

* Inverse of a permutation (this is exactly that).
* Check if an array is a valid permutation.
* Apply permutation to an array.
* Rearrange elements by index mapping.
* Construct inverse mapping in dictionaries/maps.

---

### **How to Face Similar Questions in Future**

1. **Recognize permutation structure** (unique elements in `[0, n-1]`).
2. **Think in terms of mapping**:

   * Normal array: index → value.
   * Inverse array: value → index.
3. **Use extra array first** — it’s clean and efficient for OAs.
4. **Only consider in-place encoding** if interviewer explicitly asks for space optimization.
5. **Practice related permutation problems** to quickly spot “inverse” patterns.


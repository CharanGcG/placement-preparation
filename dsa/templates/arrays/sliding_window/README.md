# Sliding Window Technique

The **Sliding Window** technique is a powerful method for solving problems involving contiguous segments (subarrays or substrings) of arrays or strings. It helps optimize brute-force solutions, reducing time complexity from O(n×k) to O(n) in many cases.

## Why Use Sliding Window?

- Efficiently process subarrays/substrings without redundant calculations.
- Ideal for problems involving sums, averages, or other aggregate functions over segments.
- Reduces nested loops to single-pass solutions.

---

## Types of Sliding Window

### 1. Fixed-Size Sliding Window

**Use Case:**  
When the window size is known and constant (e.g., "maximum sum of any subarray of size k").

**Approach:**
- Calculate the sum (or other aggregate) for the first window.
- Slide the window by one position: add the new element, remove the old one.
- Update the answer as needed.

**Example:**
```python
def sliding_window_fixed_size(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---

### 2. Variable-Size Sliding Window

**Use Case:**  
When the window size changes dynamically to meet a condition (e.g., "smallest subarray with sum ≥ target").

**Approach:**
- Use two pointers (`left` and `right`) to define the window.
- Expand the window by moving `right`.
- Shrink the window by moving `left` until the condition is met or violated.

**Example:**
```python
def sliding_window_variable_size(arr, target):
    left = 0
    cur_sum = 0
    min_length = float('inf')
    for right in range(len(arr)):
        cur_sum += arr[right]
        while cur_sum >= target:
            min_length = min(min_length, right - left + 1)
            cur_sum -= arr[left]
            left += 1
    return min_length if min_length != float('inf') else 0
```

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---

## Common Applications

- Maximum/minimum sum subarray of size k
- Longest substring with at most K distinct characters
- Smallest subarray with sum ≥ target
- Moving averages
- Problems involving frequency/counts in a window

---

## Tips & Pitfalls

- Always initialize your window correctly.
- For variable-size windows, ensure you handle edge cases (e.g., empty window, no valid subarray).
- The sliding window can be adapted for strings, 2D arrays, and more complex conditions.

---

## Further Reading

- [LeetCode Sliding Window Patterns](https://leetcode.com/tag/sliding-window/)
- [GeeksforGeeks Sliding Window](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Educative: Sliding Window Pattern](https://www.educative.io/edpresso/what-is-the-sliding-window-technique)

---

## Summary Table

| Feature         | Fixed-Size         | Variable-Size         |
|-----------------|--------------------|-----------------------|
| Window length   | Known (k)          | Flexible              |
| When to shrink  | Always after add   | Only if condition met |
| Use cases       | Max sum, averages  | Min/Max length, constraints |

---


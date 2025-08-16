# DSA Specific Tips

## Tip 1: Should I Sort the Array?

**Question:**  
“If I shuffle the array, will the answer change?”

- **If No:**  
  Sorting might help. Problems where the answer is independent of the original order (e.g., finding the largest/smallest, frequency counts) can often be solved efficiently by sorting.

- **If Yes:**  
  Sorting will likely break the logic. You need an order-preserving approach (e.g., two pointers, sliding window, dynamic programming) because the order of elements is important
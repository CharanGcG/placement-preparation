# 📘 Problem Documentation: **Sum of Digits for Each Number**

---

### **Problem Statement**

Given an array of integers, return a new array where each element is the **sum of digits** of the corresponding number.

* The numbers can be positive or negative.
* The result should always be non-negative (sum of digits ignores the sign).

---

### **Example Test Cases**

#### Example 1

```
Input:  [12, 34, 56]
Output: [3, 7, 11]
```

**Explanation:**

* 12 → 1 + 2 = 3
* 34 → 3 + 4 = 7
* 56 → 5 + 6 = 11

---

#### Example 2

```
Input:  [99, 123, 400]
Output: [18, 6, 4]
```

**Explanation:**

* 99 → 9 + 9 = 18
* 123 → 1 + 2 + 3 = 6
* 400 → 4 + 0 + 0 = 4

---

#### Example 3

```
Input: [-45, 67]
Output: [9, 13]
```

**Explanation:**

* -45 → 4 + 5 = 9 (ignore sign)
* 67 → 6 + 7 = 13

---

---

### **Approach to Consider**

1. **Digit Extraction (Math Method)**

   * For each number, take absolute value.
   * Repeatedly take `n % 10` to get last digit.
   * Add to sum.
   * Do `n //= 10` until `n = 0`.

2. **String Conversion (Easier Method)**

   * Convert number to string.
   * Iterate over characters, convert to int, and sum digits.
   * Handle negative sign properly by ignoring it.

---

### **Solution (Python — Math Method)**

```python
def sum_of_digits_array(arr):
    result = []
    for num in arr:
        n = abs(num)
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        result.append(s)
    return result
```

---

### **Solution (Python — String Conversion)**

```python
def sum_of_digits_array(arr):
    return [sum(int(d) for d in str(abs(num))) for num in arr]
```

---

### **Complexity**

* Time: **O(N \* D)**, where `N` = number of elements, `D` = average digits per number.
* Space: **O(N)** for the result array.

---

### **Related Questions**

* Digital root of a number (keep summing digits until one digit remains).
* Check if a number is divisible by 3 or 9 using digit sum.
* Transform array elements with digit-based operations.
* Sum of digits of factorial / power values.

---

### **How to Face Similar Questions in Future**

1. **Spot digit operations** — they usually involve `% 10` and `// 10` patterns.
2. **Check constraints**:

   * Negative numbers → take absolute value.
   * Very large numbers → string method is simpler.
3. **Think of both methods** (math vs. string) → choose based on time.
4. **Practice digit-based tricks** (digital root, palindrome numbers, Armstrong numbers).



---


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


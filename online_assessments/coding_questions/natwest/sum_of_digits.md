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


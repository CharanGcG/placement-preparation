# 📘 Notes on Prefix Sum

## 1. **Definition**

* Prefix sum at index `i` = sum of all elements from the start of the array up to index `i`.
* Formula:

  $$
  prefix[i] = arr[0] + arr[1] + \dots + arr[i]
  $$

---

## 2. **Purpose**

* Helps answer **range sum queries** quickly.
* Transforms subarray sum problems into a lookup problem.

---

## 3. **Construction**

For an array `arr` of size `n`:

```python
prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]
```

---

## 4. **Range Sum Query**

To find sum of subarray `arr[l..r]`:

$$
sum(l, r) = prefix[r] - prefix[l-1]  \quad (l > 0)
$$

$$
sum(0, r) = prefix[r]
$$

✅ O(1) query after O(n) preprocessing.

---

## 5. **When Prefix Sums Repeat**

* If `prefix[i] = prefix[j]` (with `i < j`), then subarray `(i+1..j)` has sum `0`.
* This is **only possible if negative numbers are present**.
* Example: `arr = [3, -1, -2, 4]` → prefix = `[3, 2, 0, 4]`

  * `prefix[2] = 0` and initial `prefix = 0` → subarray `[0..2]` sums to `0`.

---

## 6. **Prefix Sum + Hashmap**

Instead of storing an array, we store prefix sums in a **map/dictionary**:

* **Why?**

  * To check if `prefix[i] - target` exists.
  * This tells us if a subarray ending at `i` has sum = `target`.

* **Two modes of hashmap storage**:

  1. **Store first index** → helps find *where* the subarray starts.
  2. **Store frequency** → helps count *how many* such subarrays exist.

---

## 7. **Applications**

1. **Subarray sum problems**

   * Find if subarray with sum = `k` exists.
   * Count number of subarrays with sum = `k`.

2. **Zero-sum subarrays**

   * If same prefix appears again, subarray in between has sum `0`.

3. **Range queries**

   * Given multiple `(l, r)` queries → prefix sum answers them in O(1).

4. **2D Prefix Sum (Matrix)**

   * For submatrix sums: precompute `prefix[i][j] = sum of rectangle (0,0) → (i,j)`

---

## 8. **Complexity**

* Preprocessing: **O(n)**
* Query: **O(1)**
* With hashmap: Finding/counting subarrays = **O(n)** average.

---

## 9. **Quick Analogy**

Think of prefix sums like a **running balance in a bank account**:

* `prefix[i]` = balance after day `i`.
* If at two different days the balance is the same, the transactions in between must sum to zero.
* If today’s balance minus an earlier balance = `target`, then the transactions in between sum to `target`.

---

✅ That’s the full picture: **definition → intuition → formula → hashmap trick → applications**.

---


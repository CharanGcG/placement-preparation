Here is your content, exactly as provided, in markdown format for a README file:

***

## 20 MCQs, 2 Coding Questions, 1 Design Question

***

### MCQ Topics

- **Java code given, predict output**
- **DBMS - SQL queries, ACID properties**
- **Operating systems - deadlock, scheduling algorithms**

***

## Coding Questions

***

### 1. Largest Square of '1's in a Grid

Given a grid of n x m size consisting of '0's and '1's, we need to find the area of the largest square consisting of only '1's.  
(we need to use dp)

We’re asked:  
👉 Given an `n x m` binary grid, find the **largest square** consisting only of `'1'`. Return its **area** (side × side).

***

#### 🧠 Key Idea

* If you’re at a cell `(i, j)` that contains `'1'`, the largest square that can end at `(i, j)` depends on its **neighbors**:

  * `(i-1, j)` → above  
  * `(i, j-1)` → left  
  * `(i-1, j-1)` → diagonal

* Recurrence:

  ```
  dp[i][j] = 0                                  if grid[i][j] == '0'
  dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1   if grid[i][j] == '1'
  ```

* `dp[i][j]` means: the **side length of the largest square ending at (i, j)**.

* The maximum value in `dp` will be the side of the largest square.
  Final answer = `max_side^2`.

***

#### ⚡ Steps

1. Initialize `dp` of same size as grid (or do it in-place).
2. First row & column: `dp[i][j] = 1` if grid[i][j] = '1'.
3. Fill table using recurrence.
4. Track the maximum side length while filling.
5. Return area = `max_side^2`.

***

#### ⌨️ Example

Grid:

```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

DP table evolves into:

```
1 0 1 0 0
1 0 1 1 1
1 1 1 2 2
1 0 0 1 0
```

Max side = 2 → Area = 4.

***

#### 🐍 Python Implementation

```python
def maximalSquare(matrix):
    if not matrix:
        return 0
    
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    max_side = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                    ) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side
```

***

### 2. Sum of Minimums Over All Subarrays

Given an array, we need to divide the array into subarrays of different lengths, then add the minimum of each subarray and return it:  
example: arr =
, , ,  : 1 + 2 + 3 + 4 = 10  
   : 1 + 2 + 3 = 6
  : 1 + 2 = 3
 : 1

final result = 10 + 6 + 3 + 1 = 20

(we need to use monotonic stack)

***

## Code Trace

### Initial

```
arr = [3, 1, 2, 4]
n = 4
left = [0,0,0,0]
right = [0,0,0,0]
```

***

### Pass 1: Build `left` (previous less element counts)

> Rule: while stack top > arr[i], pop.  
> Each popped count gets added.

* i=0, arr\=3  
  stack empty → count=1  
  left\=1  
  stack=[(3,1)]

* i=1, arr\=1  
  stack top 3 > 1 → pop (3,1), count=2  
  left\=2  
  stack=[(1,2)]

* i=2, arr\=2  
  stack top 1 > 2? No (1 < 2)  
  count=1  
  left\=1  
  stack=[(1,2),(2,1)]

* i=3, arr\=4  
  stack top 2 > 4? No  
  count=1  
  left\=1  
  stack=[(1,2),(2,1),(4,1)]

Result:

```
left = [1, 2, 1, 1]
```

***

### Pass 2: Build `right` (next less-or-equal counts)

> Rule: while stack top >= arr[i], pop.  
> Each popped count gets added.

* i=3, arr\=4  
  stack empty → count=1  
  right\=1  
  stack=[(4,1)]

* i=2, arr\=2  
  stack top 4 >= 2 → pop (4,1), count=2  
  right\=2  
  stack=[(2,2)]

* i=1, arr\=1  
  stack top 2 >= 1 → pop (2,2), count=3  
  right\=3  
  stack=[(1,3)]

* i=0, arr\=3  
  stack top 1 >= 3? No (1 < 3)  
  count=1  
  right\=1  
  stack=[(1,3),(3,1)]

Result:

```
right = [1, 3, 2, 1]
```

***

### Pass 3: Contributions

Formula: `arr[i] * left[i] * right[i]`

* i=0 → 3 \* 1 \* 1 = 3  
* i=1 → 1 \* 2 \* 3 = 6  
* i=2 → 2 \* 1 \* 2 = 4  
* i=3 → 4 \* 1 \* 1 = 4

Sum = 17

✅ Correct (matches brute force check).

***

## 📊 Intuition

* `left[i]` = how many ways I can extend **to the left** while still being the minimum.
* `right[i]` = how many ways I can extend **to the right** while still being the minimum.
* `arr[i]` contributes in exactly `left[i] * right[i]` subarrays.

***



---


## Design question

We needed to design an online food ordering app using oops showing all the four pillars, syntax was not given importance, the content was important
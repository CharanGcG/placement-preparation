# Pen and Paper Test Experience (NI Emerson)

---

First time facing pen and paper test during placements.  
Consisted of ten questions, without any options; we needed to solve the problem and write the final answer on the front sheet.

---

## Questions:

1. **A book is numbered from page 1 to a certain number of pages, one of the page numbers is duplicated. If the sum of all page numbers is 1000, which is the page number that is duplicated?**

2. **A C program that converts a string into palindrome in place:**  
   Example: `world` → `dlrld`

3. **A C program dealing with pointers and pointer to pointers**

4. **If A can solve a problem with probability 1/2 and B can solve in 3/4, A, B and C together can solve it with 63/64. What is the probability that C can solve it alone?**

5. **There is a certain number of rats R that start at E for a rectangle EFGH. There is a cat that eats C number of rats along each edge equally. The number of rats doubles at F, triples at G, quadruples at H. Given that the number of rats reaching F, G, H is non zero and reaching E is zero, what is the minimum value of (R, C)?**

6. **There are seven stepping stones on a river. You have to find the number of ways you could reach the other side of the river if you can either take one step or two steps at a time. Also give the recursive equation.**

7. **Consider 7 digit numbers that only contain digits 2 or 3. How many such numbers are multiples of 12?**

8. **Consider f(a, b) returns the number of orientations you could have of the shape 'L' within the a × b grid. What is the possible equation of f(a, b)?**

9. **Three ways to get Fibonacci sequence: DP, recursion, memoization. Arrange them in increasing order of time complexity.**

10. **Question based on instructions related to assembly style code:**  
    Each instruction takes 6 cycles to complete. If two or more successive instructions are independent of each other, they can execute parallelly, with one instruction starting after one cycle of the previous. So if there are two independent instructions, it takes 7 cycles to complete; if they are dependent, it takes 12 cycles. Given 10 instructions, we were asked to find the minimum number of cycles needed to execute the instructions in (a) the given order (b) any random order.

---


# Pen and Paper Test Solutions (NI Emerson)

---

## 1. Duplicated page with sum 1000

Let the book have pages `1..n`. If page `k` is duplicated:

$$
\frac{n(n+1)}{2} + k = 1000
$$

Solving gives $n=44$, $k=10$.

**Answer:** **10** (book has 44 pages; page 10 counted twice).

---

## 2. C: Convert a string to a palindrome in-place

For each mirrored pair, set both to the **min** of the two chars. Example: `world` → `dlrld`.

```c
#include <stdio.h>
#include <string.h>

void to_palindrome(char *s) {
    int i = 0, j = (int)strlen(s) - 1;
    while (i < j) {
        char c = s[i] < s[j] ? s[i] : s[j];
        s[i] = s[j] = c;
        i++; j--;
    }
}

int main() {
    char s[] = "world";
    to_palindrome(s);
    printf("%s\n", s); // prints: dlrld
    return 0;
}
```

---

## 3. C: Pointers and pointer-to-pointer

```c
#include <stdio.h>
#include <stdlib.h>

void incr(int *p) { (*p)++; }
void reassign(int **pp, int *to) { *pp = to; }

int main() {
    int a = 10, b = 99;
    int *p = &a;
    incr(p);                 // a = 11
    reassign(&p, &b);        // p now points to b
    incr(p);                 // b = 100
    printf("a=%d b=%d *p=%d\n", a, b, *p); // 11, 100, 100
    return 0;
}
```

---

## 4. Probability for C alone

$$
P(\text{none}) = (1-\tfrac12)(1-\tfrac34)(1-p_C) = \tfrac18(1-p_C)
$$

$$
P(\text{at least one}) = 1 - \tfrac18(1-p_C) = \tfrac{63}{64}
$$

$$
1 - p_C = \tfrac{1}{8} \implies p_C = \boxed{\tfrac{7}{8}}
$$

---

## 5. Rats around rectangle (min integers)

Smallest positive integer solution with nonzero F,G,H:

$$
\boxed{R=41,\; C=24}
$$

---

## 6. 7 stepping stones; steps of 1 or 2

Recurrence: $T(n)=T(n-1)+T(n-2)$, with $T(0)=1,\; T(1)=1$.

For 7 stones: $T(7)=F_{8}= \boxed{21}$.

---

## 7. 7-digit numbers of only 2s and 3s that are multiples of 12

Divisible by 12 ⇒ divisible by 3 and 4.

- Mod 3: sum of digits $= 14 + k$ where $k$ is number of 3s. Need $k\equiv 1 \pmod 3$.
- Mod 4: last two digits must be 32.

Total $\boxed{11}$ such numbers.

---

## 8. Count L-shapes in an $a\times b$ grid

**Formula 1 (for 2×2 tromino L):**

$$
f(a,b)=4\,(a-1)(b-1)
$$

**Formula 2 (for general rectangular L):**

$$
f(a,b) = a(a-1)\, b(b-1)
$$

---

## 9. Fibonacci methods by increasing time complexity

- **DP (tabulation):** $O(n)$
- **Memoization (top-down):** $O(n)$
- **Naive recursion:** $O(\varphi^n)$ (exponential)

**Order:** $\boxed{\text{DP} \approx \text{Memoization} < \text{Naive Recursion}}$

---

## 10. Instruction cycles with overlap

- **Best possible (all independent):** $10+5=\boxed{15}$ cycles.
- **Worst case (all dependent):** $6\times10=\boxed{60}$ cycles.
- **General method:** Partition into maximal independent runs; total is $\sum_i (k_i+5)$ where $k_i$ are run lengths.

---
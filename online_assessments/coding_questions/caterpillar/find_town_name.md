
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


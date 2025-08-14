# Creation
arr = [3, 1, 4, 1, 5]
arr2 = list((9, 2, 6))

# Manipulation
arr.append(9)
arr.extend(arr2)
arr.insert(2, 8)
arr.remove(1)
popped = arr.pop()
arr.reverse()
arr_copy = arr.copy()
arr.clear()
arr = arr_copy
arr_copy.clear()
arr = [3, 1, 4, 1, 5]

# Searching
pos = arr.index(4)
cnt = arr.count(1)
exists = 5 in arr

# Sorting
arr.sort()
arr.sort(reverse=True)
sorted_arr = sorted(arr)
sorted_desc = sorted(arr, reverse=True)

# Iteration
for num in arr:
    pass
i = 0
while i < len(arr):
    i += 1
squares = [x**2 for x in arr]

# Extra Methods
arr3 = [10, 20]
arr += arr3
arr *= 2
arr_copy = arr.copy()
arr_copy.reverse()
arr_copy.sort()
p = arr_copy.pop(0)
arr_copy.append(99)
arr_copy.insert(1, 88)
arr_copy.extend([77, 66])
arr_copy.remove(99)
c = arr_copy.count(88)
idx = arr_copy.index(88)
arr_copy.clear()

# Built-ins interacting with lists
length = len(arr)
minimum = min(arr)
maximum = max(arr)
total = sum(arr)
any_true = any([0, 1])
all_true = all([1, 2, 3])
enumerated = list(enumerate(arr))
zipped = list(zip(arr, arr2))
flattened = [item for sublist in [[1, 2], [3, 4]] for item in sublist]

def get_prefix_sum(arr):
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    return prefix_sum


def range_sum(prefix_sum, left, right):
    return prefix_sum[right + 1] - prefix_sum[left]


def prefix_sum_hashmap(arr, target):
    prefix_sum = 0
    hashmap = {0: 1}
    count = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum - target in hashmap:
            count += hashmap[prefix_sum - target]
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    return count
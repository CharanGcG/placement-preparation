def sliding_window_fixed_size(arr, k):
    '''
    k: window size
    sum: the operation performed on the window - can vary based on question
    '''
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def sliding_window_variable_size(arr, target):
    '''
    target: target that the window has to achieve
    min_len: minimum length of the window which achieves the target
    '''
    left = 0
    cur_sum = 0
    for right in range(len(arr)):
        cur_sum += arr[right]
        while cur_sum > target:
            min_len = min(min_len, right - left + 1)
            cur_sum -= arr[left]
            left += 1
    return min_len if min_len != float('inf') else 0


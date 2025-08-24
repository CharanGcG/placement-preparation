# My initial code from scratch from paper to code
def merge(intervals):
    intervals.sort(key=lambda x : x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged


# Cleaner code: Merging intervals : we sort by starting time
def merge(intervals):
    intervals.sort(key=lambda x : x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if last_end >= start:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged


# When removing minimum number of intervals to make others non overlapping, we sort by end time
# This is to retain as many intervals as we could
def remove(intervals):
    intervals.sort(key=lambda x: x[1])  # Here is the difference
    merged = [intervals[0]]
    overlapping_intervals = 0

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if last_end > start:
            overlapping_intervals += 1
        else:
            merged.append([start, end])
    return overlapping_intervals
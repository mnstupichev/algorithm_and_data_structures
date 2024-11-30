def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


with open('/lab2/task1/textf/input', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

sorted_arr = merge_sort(arr)

with open('/lab2/task1/textf/output', 'w') as f:
    f.write(' '.join(map(str, sorted_arr)))

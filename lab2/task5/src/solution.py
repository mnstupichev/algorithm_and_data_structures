def majority_element(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_majority = majority_element(arr[:mid])
    right_majority = majority_element(arr[mid:])

    if left_majority == right_majority:
        return left_majority

    count_left = arr.count(left_majority) if left_majority else 0
    count_right = arr.count(right_majority) if right_majority else 0

    if count_left > len(arr) // 2:
        return left_majority
    elif count_right > len(arr) // 2:
        return right_majority
    else:
        return None


with open('/lab2/task5/textf/input', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

ans = None
if majority_element(arr) is not None:
    ans = 1
else:
    ans = 0

with open('/lab2/task5/textf/output', 'w') as f:
    f.write(str(ans))

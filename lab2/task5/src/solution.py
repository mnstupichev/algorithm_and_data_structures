from utils import read, write


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


def main():
    array, = read()
    majority = majority_element(array)
    if majority is not None:
        majority = 1
    else:
        majority = 0
    write(majority)


if __name__ == "__main__":
    main()


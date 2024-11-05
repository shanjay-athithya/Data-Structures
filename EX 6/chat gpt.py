def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + equal + quicksort(right)


if __name__ == '__main__':
    arr = [3, 7, 1, 99, 0, 34, 8, 3, 999]
    sorted_arr = quicksort(arr)
    print(sorted_arr)

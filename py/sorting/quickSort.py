def quickSort(arr):
    if len(arr) <=1:
        return arr
    pivot =  arr[0]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + mid + quickSort(right)


if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quickSort(arr))
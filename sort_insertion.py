def insertionSort(arr):
    length = len(arr)

    # naive solution
    for i in range(1, length):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

    # optimized solution
    for i in range(1, length):
        currentVal = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > currentVal:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = currentVal

    return arr


arr = [3,7,8,4,12,10,18]
insertionSort(arr)

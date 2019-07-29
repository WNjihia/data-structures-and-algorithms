def selectionSort(arr):
    length = len(arr)

    for i in range(length):
        min = i
        for j in range(i+1, length):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

    return arr

arr = [2,6,5,17,13,10] # [2,5,6,10,13,17]
print(selectionSort(arr))

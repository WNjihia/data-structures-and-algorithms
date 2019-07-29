def bubbleSort(arr):
    # naive solution
    length = len(arr)
    temp = 0

    for i in range(length):
        for j in range(length-1):
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

    # first optimization - so we don't loop over the last items since they've been sorted
    for i in range(length):
        for j in range(length-i-1):
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

    # second optimization solution with swapped
    for i in range(length): #0 #1
        swapped = False
        for j in range(length - i - 1): #4 #3
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break;

    return arr


arr = [8,1,2,3,4]
bubbleSort(arr)

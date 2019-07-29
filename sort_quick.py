def pivotHelper(arr, start, endIndex):
    swapIndex = start

    for i in range(start+1, endIndex+1):
        if arr[start] > arr[i]:
            swapIndex += 1
            arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
    arr[start], arr[swapIndex] = arr[swapIndex], arr[start]

    return swapIndex

def quickSort(arr, left=0, right=None):
    if right == None:
        right = len(arr)-1

    if left < right:
        pivotIndex = pivotHelper(arr, left, right)
        quickSort(arr, left, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, right)
    return arr


arr = [4,8,2,1,5,7,6,3]
print(quickSort(arr))

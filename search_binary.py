def binarySearchIterative(arr, val):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        # middle = int((left + right)/2)
        middle = (left + right) // 2

        if arr[middle] == val:
            return middle

        if arr[middle] < val:
            left = middle + 1
        else:
            right = middle - 1

    return -1

def binarySearchRecursive(arr, val, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return -1

    # middle = int((left + right) / 2)
    middle = (left + right) // 2

    if arr[middle] == val:
        return middle

    if arr[middle] < val:
        return binarySearchRecursive(arr, val, middle+1, right)
    else:
        return binarySearchRecursive(arr, val, left, middle-1)

# def binarySearchRecursive2(arr, val):
#     length = len(arr)
#
#     if length == 0:
#         return -1
#
#     middle = int(length/2)
#
#     if arr[middle] == val:
#         return middle
#
#     if arr[middle] < val:
#         return binarySearchRecursive(arr[middle+1:], val)
#     else:
#         return binarySearchRecursive(arr[:middle-1], val)


arr = [1,2,3,5,6,8]
print(binarySearchIterative(arr, 1))
print(binarySearchRecursive(arr, 1))
# print(binarySearchRecursive2(arr, 6))

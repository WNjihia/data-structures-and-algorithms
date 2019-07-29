def linearSearch(arr, val):
    length = len(arr)

    for i in range(length):
        if arr[i] == val:
            return i
    return -1


print(linearSearch([1,2,3,4], 6))
print(linearSearch([1,2,3,4], 4))

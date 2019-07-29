def merge(arr1, arr2):
    length1 = len(arr1)
    length2 = len(arr2)
    i = j = 0
    sorted_arr = []

    while i < length1 and j < length2:
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < length1:
        sorted_arr.append(arr1[i])
        i += 1

    while j < length2:
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


def mergeSort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])

    return merge(left, right)



print(mergeSort([10,24,76,73]))

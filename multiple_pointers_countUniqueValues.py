def countUniqueValues(arr):
    length = len(arr)
    if length == 0:
        return "0"

    value = arr[0]
    uniqueValues = 1

    for i in range(1, length):
        if arr[i] != value:
            uniqueValues += 1
            value = arr[i]
    return uniqueValues

        # for item in arr:
        #     if item != value:
        #         uniqueValues += 1
        #         value = item


countUniqueValues([1,1,1,1,1,2])
countUniqueValues([])
countUniqueValues([-2,-1,-1,0,1])
countUniqueValues([1,2,3,4,4,4,7,7,12,12,13])

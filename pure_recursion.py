def collectOddValues(arr):
    oddValues = []

    if len(arr) == 0:
        return oddValues;

    if arr[0] % 2 != 0:
        oddValues.append(arr[0])

    del arr[0]

    oddValues = oddValues + collectOddValues(arr)
    return oddValues


print(collectOddValues([1,2,3,4,5]))

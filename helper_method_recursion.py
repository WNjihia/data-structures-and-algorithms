# collect odd values in array

def collectOddValues(arr):
    oddValues  = []

    def checkIfOdd(arr):
        if len(arr) == 0:
            return;

        if arr[0] % 2 != 0:
            oddValues.append(arr[0])

        del arr[0]
        checkIfOdd(arr)

    checkIfOdd(arr)

    return oddValues


print(collectOddValues([1,2,3]))

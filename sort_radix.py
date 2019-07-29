import math

def getDigit(num, place):
    num = abs(num)
    return (num // 10 ** place) % 10

def getDigitCount(num):
    # using log
    num = abs(num)
    if num == 0:
        return 1
    return math.floor(math.log(num, 10) + 1)

def mostDigits(arr):
    maxDigits = 0
    for num in arr:
        temp = getDigitCount(num)
        if temp > maxDigits:
            maxDigits = temp
    return maxDigits

def radixSort(arr):
    maxDigitCount = mostDigits(arr)
    length = len(arr)
    for i in range(maxDigitCount):
        sorted = {}

        for k in range(length):
            temp = []
            position = getDigit(arr[k], i)
            temp.append(arr[k])
            if position not in sorted:

                sorted[position] = temp
            else:
                sorted[position] = sorted[position] + temp
        print(sorted)

        sortedArr = []
        for key, value in sorted.items():
            sortedArr = sortedArr + value
            print(sortedArr)

print(radixSort([23, 1, 567, 89, 1234434, 3]))

def maxSubArraySum(arr, num):
    length = len(arr)
    # if length < num:
    #     return None

    maxSum = 0

    for i in range(num):
        maxSum += arr[i]

    tempSum = maxSum

    for j in range(num, length):
        tempSum  = tempSum + arr[j] - arr[j - num]
        if tempSum > maxSum:
            maxSum = tempSum

    print(maxSum)

# maxSubArraySum([], 4)
maxSubArraySum([1,2,5,2,8,1,5], 4)
maxSubArraySum([1,2,5,3], 2)
maxSubArraySum([2,6,9,2,1,8,5,6,3], 3)

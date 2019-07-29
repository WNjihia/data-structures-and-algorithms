def naiveSearch(longStr,shortStr):
    length = len(longStr)
    innerLength = len(shortStr)
    count = 0
    i = 0
    j = 0

    # for i in range(length):
    #     for j in range(innerLength):
    #         if shortStr[j] != longStr[i+j]:
    #             break
    #
    #         if j == innerLength - 1:
    #             count += 1
    #
    # return count

    while i < length:
        if shortStr[j] != longStr[i+j]:
            i += 1
            j = 0
        else:
            j += 1

        if j == innerLength - 1:
            count += 1
            i += 1
            j = 0


    return count


longStr = "wowomgzomg"
shortStr = "omg"

print(naiveSearch(longStr,shortStr))

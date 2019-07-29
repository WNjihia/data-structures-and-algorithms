# Find whether string S is periodic.
# Periodic indicates S = nP.
# e.g.
# S = "ababab", then n = 3, and P = "ab"
# S = "xxxxxx", then n = 1, and P = "x"
# S = "aabbaaabba", then n = 2, and P = "aabba"
# follow up:
# Given string S, find out the P (repetitive pattern) of S.


def checkPeriodic(S):
    length = len(S)
    subStr = ""

    if length <= 1:
        return "Not Periodic"

    for i in range(length):
        subStr = subStr + S[i]

        subStrLength = len(subStr)
        temp = subStr * (int(length/subStrLength))

        if temp == S and subStr != S:
            return "Periodic"

    return "Not Periodic"


S = "aa"
print(checkPeriodic(S))

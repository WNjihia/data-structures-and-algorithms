# Example 1
def countDown(num):
    if num <= 0:
        print("All Done")
        return;

    print(num)
    num -= 1
    countDown(num)

countDown(3)

# Example 2
def sumRange(num):
    if num == 1:
        return 1

    return num + sumRange(num - 1)


print(sumRange(3))

# Example 3
def factorial(num):
    # 4! = 4 * 3 * 2 * 1

    if num == 1:
        return 1

    return num * factorial(num - 1)

print(factorial(4))

# Please write a program which asks the user to type in a limit.
# The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...)
# until the sum is at least equal to the limit set by the user

limit = int(input("Limit:"))

consecutiveSum = 1
resultSum = 0
result = "The consecutive sum: "

while consecutiveSum < limit:

    result += f"{consecutiveSum}"

    consecutiveSum += 1

    resultSum += consecutiveSum

    if consecutiveSum != limit:
        result += " + "

print(f"{result} = {consecutiveSum}")
def plusOne(digits):
    count = 1
    sum = 0
    for i in range(len(digits)):
        sum += digits[-(i + 1)] * count
        count *= 10
    sum += 1
    # print(sum)
    sum1 = str(sum)
    print(sum1)
    # sum2 = sum1.split()
    sum2 = list(sum1)
    sum2 = list(map(int, sum2))
    return sum2
digits = [9]
print(plusOne(digits))
def make_sum (numbers):
    result = 0
    for i in range (len(numbers)):
        temp = 0
        for j in str(numbers[i]):
            temp += int(j)
        if temp % 7 == 0:
            result += numbers[i]
    return result
cubs = [item ** 3 for item in range (1,1000, 2)]
print(make_sum(cubs))
for i in range (len(cubs)):
    cubs[i] += 17
print(make_sum(cubs))
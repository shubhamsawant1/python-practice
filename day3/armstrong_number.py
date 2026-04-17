num = 584
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10
print(sum)
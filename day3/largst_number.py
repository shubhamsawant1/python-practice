num = 5832
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
     largest = digit
    num //= 10
print(largest)
    
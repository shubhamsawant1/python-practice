evencount = 0
oddcount = 0

for num in range(1 , 51):
    if num % 2 == 0:
        evencount += 1
    else:
        oddcount += 1
    num += 1

print("even count: ", evencount)
print("odd count: ", oddcount)
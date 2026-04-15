# print numbers 1 to 30 but  if divisible divisible by 3 print fizz if divisible 
# by 5 print buzz and if both print fizzbuzz

num = 1

while num <= 30:
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    num += 1

# using for loop

num2 = 1

for num2 in range(1 , 31):
    if num2 % 3 == 0:
        print(num2)
    num2 += 1
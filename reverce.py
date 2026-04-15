#print reverse 10 to 1 even numbers

num = 10

while num >= 1 :
    if num % 2 == 0:
     print(num)
    num -= 1

# using for loop 

num2 = 10

for num2 in range(10, 0, -1):
   if num2 % 2 == 0:
      print(num2)
   num2 -= 1
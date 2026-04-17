num = 12
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
    
print(factors)

student = int(input("Enter a number: "))
names = []

for i in range(student):
    name = input("enter name of student: ")
    names.append(name)

print(names)
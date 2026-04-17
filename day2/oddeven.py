num = 1
evencount = 0
oddcount = 0

while num <= 30:
    if num % 2 == 0:
        print("even number", num)
        evencount += 1
    else: 
        print("odd number" ,num)
        oddcount += 1
    num += 1

print("the number of even number is: ", evencount)
<<<<<<< HEAD
print("the number of odd nnumber is: " , oddcount) 
=======
print("the number of odd nnumber is: " , oddcount)
>>>>>>> f288d80 (update)

# cleaner version (for loop)
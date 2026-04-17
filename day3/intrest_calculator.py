# Question3 : Build a simple intrest calculator
# Input : principal (p) rate (R) time(t)
# output : (P*R*T)/100

priAmount = float(input("enter the principal amount : "))
rate = float(input("enter the rate of intrest : "))
time = float(input("enter the time : "))

simpleIntrest = (priAmount * rate * time) / 100
print("the simple intrest is : " + str(simpleIntrest))

# 1. Write a Python program to check if a given number is prime.


p = True
n = int(input("Enter the number: "))

for i in range(2,int(n*0.5)):
    if n % i == 0:
        p = False
    
if (p):
    print("The given number is prime.")
else:
    print("The given number is not  prime.")

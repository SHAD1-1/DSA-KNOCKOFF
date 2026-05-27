#Take two integers from the user. 
# Fill an integer array of size 25 with random values between the two numbers given by the user. 
# Print the array.

import random

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

arr = []

for i in range(25):
    num = random.randint(num1, num2)
    arr.append(num)
    
print(arr)
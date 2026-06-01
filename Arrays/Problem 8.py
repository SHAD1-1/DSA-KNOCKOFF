#Fill an integer array with random values. Separate the even values and store them inan array named evenArray and the odd numbers in another array named oddArray. Print all three arrays.

import random 

arr1 = []
arreven = []
arrodd = []

for i in range(10):
    num = random.randint(0, 100)
    arr1.append(num)

for i in range(10):
    if arr1[i] % 2 == 0:
        arreven.append(arr1[i])
    else:
        arrodd.append(arr1[i])

print("Original Array:", arr1)
print("Even Array:", arreven)
print("Odd Array:", arrodd)


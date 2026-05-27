#Ask the user to enter the size of an array. 
# Create an integer array of the given size and fill it with random numbers.
#  Print the array then take another number from the user and search that number in the array. 
# If the value is found, print the indices (plural of index) where the value was found.
#  Also print how many times the value was found in the array.


import random

size = int(input("Enter array size: "))
arr = []

for i in range(size):
    num = random.randint(0, 999)
    arr.append(num)

print(arr)

num = int(input("Enter a number: "))

count = 0

for i in range(size):
    if arr[i] == num:
        print(f"Index {i}")
        count += 1

print(f"Number {num} found {count} times")
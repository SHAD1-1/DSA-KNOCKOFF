# Find the largest, smallest and average in an array.

import random

size = int(input("Enter array size: "))
arr = []

for i in range(size):
    arr.append(random.randint(0, 10))

largest = arr[0]
smallest = arr[0]
count = 0

for i in arr:

    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

    count += i

average = count / size

print("Array:")
print(arr)

print("\nLargest =", largest)
print("Smallest =", smallest)
print("Average =", average)
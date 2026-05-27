#_ Create two floating point arrays. Fill them with random numbers.
#  Sort the first array in descending order and the second array in ascending order.
#  Print both arrays before and after sorting.
import random

arr1 = []
arr2 = []

# Fill both arrays with random floating numbers
for i in range(10):
    num = random.uniform(0, 100)
    arr1.append(round(num, 2))

for i in range(10):
    num = random.uniform(0, 100)
    arr2.append(round(num, 2))

print("Before Sorting:")
print("Array 1:", arr1)
print("Array 2:", arr2)

# Descending sort for arr1 (without built-in sort)
for i in range(len(arr1)):
    for j in range(i + 1, len(arr1)):
        if arr1[i] < arr1[j]:
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp

# Ascending sort for arr2 (without built-in sort)
for i in range(len(arr2)):
    for j in range(i + 1, len(arr2)):
        if arr2[i] > arr2[j]:
            temp = arr2[i]
            arr2[i] = arr2[j]
            arr2[j] = temp

print("\nAfter Sorting:")
print("Array 1 (Descending):", arr1)
print("Array 2 (Ascending):", arr2)

#Find the 1st and 2nd minimum, 1st and 2nd maximum, and median of an array of size 11.
arr = []

# Take input
for i in range(11):
    num = float(input("Enter a number: "))
    arr.append(num)

print("Original Array:", arr)

# Bubble Sort
for i in range(10):
    for j in range(10 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted Array:", arr)

# Find values
first_min = arr[0]
second_min = arr[1]

first_max = arr[10]
second_max = arr[9]

median = arr[5]

print("1st Minimum:", first_min)
print("2nd Minimum:", second_min)

print("1st Maximum:", first_max)
print("2nd Maximum:", second_max)

print("Median:", median)
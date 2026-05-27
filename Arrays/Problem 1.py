#Fill an array of integers (any size) with user input and print the array forwards and backwards.

size = int(input("Enter array size: "))
arr = []

for i in range(size):
    num = int(input("Enter a number: "))

    arr.append(num)

print(f"Array forwards:{arr}")

arr1 = []

for i in range(size-1,-1, -1):
    arr1.append(arr[i])

print(f"Array backwards:",arr1)









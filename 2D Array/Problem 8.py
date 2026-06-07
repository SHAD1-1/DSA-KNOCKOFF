#Convert a 1D array of size 10 toa 2x 5 or 5 x 2 (2D) array (make sure no data is lost).

arr = []

# Input 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    arr.append(num)

arr2d = []
index = 0

# Create 2 rows and 5 columns
for i in range(2):
    row = []
    for j in range(5):
        row.append(arr[index])
        index += 1
    arr2d.append(row)

print("1D Array:")
print(arr)

print("2D Array:")
for row in arr2d:
    print(row)
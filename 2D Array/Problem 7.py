#Convert a 5x7 (2D) integer array to a 1D array.
arr = []
new_arr = []

# Input 5x7 array
for i in range(5):
    row = []
    for j in range(7):
        num = int(input("Enter a number: "))
        row.append(num)
    arr.append(row)

# Convert 2D array to 1D array
for row in arr:
    for num in row:
        new_arr.append(num)

print("2D Array:")
for row in arr:
    print(row)

print("1D Array:")
print(new_arr)
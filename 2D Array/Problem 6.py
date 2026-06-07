#Compute the average value of each of the rows of a 15 x 10 floating point array.

arr = []

# Input 15 rows and 10 columns
for i in range(15):
    row = []
    for j in range(10):
        num = float(input("Enter a number: "))
        row.append(num)
    arr.append(row)

# Calculate average of each row
for row in arr:
    total = 0

    for num in row:
        total += num

    average = total / len(row)


    print("Average =", average)
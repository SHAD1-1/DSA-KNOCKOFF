#_ Create a 5 by 5 integer matrix. Fill it with random numbers. Calculate the sum of the main diagonal and the sum of the secondary diagonal.
import random

# Create a 5x5 matrix
matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(random.randint(1, 10))
    matrix.append(row)

# Print the matrix
print("Matrix:")
for row in matrix:
    print(row)

sum1 = 0  # Main diagonal sum
sum2 = 0  # Secondary diagonal sum

for i in range(5):
    sum1 = sum1 + matrix[i][i]
    sum2 = sum2 + matrix[i][4 - i]

print("Main Diagonal Sum =", sum1)
print("Secondary Diagonal Sum =", sum2)
#Create a 4 by 3 integer matrices called A and a 3 by 2 integer matrix called B. Fill both matrices with random numbers. Multiply A and B and store the resultant matrix in C. Print A, B and C.

import random

# Create matrix A (4 x 3)
A = []
for i in range(4):
    row = []
    for j in range(3):
        row.append(random.randint(1, 10))
    A.append(row)

# Create matrix B (3 x 2)
B = []
for i in range(3):
    row = []
    for j in range(2):
        row.append(random.randint(1, 10))
    B.append(row)

# Create matrix C (4 x 2)
C = []
for i in range(4):
    row = []
    for j in range(2):
        total = 0
        for k in range(3):
            total = total + A[i][k] * B[k][j]
        row.append(total)
    C.append(row)

# Print matrices
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nMatrix C (A × B):")
for row in C:
    print(row)
#Create two 4 by 3 integer matrices called A and B. Subtract A from B and store the resultant matrix in C.Print A, B and C matrices.

import random
a = []
for i in range(4):
    row = []
    for j in range(3):
        row.append(random.randint(1, 10))
    a.append(row)
print(a)

b = []
for i in range(4):
    row = []
    for j in range(3):
        row.append(random.randint(1, 10))
    b.append(row)
print(b)

c = []
for i in range(4):

    row = []
    for j in range(3):
        row.append(a[i][j] - b[i][j])
    c.append(row)

print("Matrix A:", a, "\nMatrix B:", b, "\nMatrix C:", c)


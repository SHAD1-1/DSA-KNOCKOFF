#Take the size of a matrix, A, from the user. Create the matrix, A, and fill it with user input. Then store the transpose of A in another matrix B. Print both A and B.

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))



a = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element at position ({i} {j}): ")))
    a.append(row)

# Create the transpose of matrix A and store it in matrix B
b = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(a[i][j])
    b.append(row)

print("Matrix A:")
for row in a:
    print(row)

print("Matrix B (Transpose of A):")
for row in b:
    print(row)  

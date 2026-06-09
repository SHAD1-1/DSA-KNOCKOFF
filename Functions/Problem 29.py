#Sum of coloumns
def column_sum(matrix):
    cols = len(matrix[0])

    for j in range(cols):
        total = 0
        for i in range(len(matrix)):
            total += matrix[i][j]
        print(total)

arr = [[1, 2, 3], [4, 5, 6]]
column_sum(arr)
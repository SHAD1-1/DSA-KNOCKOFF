#Maximum element in a 2D list

def maximum(matrix):
    biggest = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > biggest:
                biggest = matrix[i][j]

    return biggest


arr = [
    [4, 2, 9],
    [1, 7, 3]
]

print(maximum(arr))


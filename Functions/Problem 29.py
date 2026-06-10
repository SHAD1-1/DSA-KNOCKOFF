#Sum of coloumns
def coloumn_sum(num):
    cols =len(num[0])

    for j in range(cols):
        total = 0
        for i in range(len(num)):
            total += num[i][j]

        print(total)

arr = [[1,2,3],[4,5,6]]
coloumn_sum(arr)

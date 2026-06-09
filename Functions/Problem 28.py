#Finding the sum of each row
def row_sum(num):
    for i in num:
        total = 0
        for j in i:
            total += j
        print(total)
arr = [[1, 2, 3], [4, 5, 6]]
row_sum(arr)
#Finding the sum sof all elements in a 2d lst



def total_sum(num):
    total = 0

    for i in num:
        for j in i:
            total += j

    return total

arr = [[1,2],[3,4]]

print(total_sum(arr))


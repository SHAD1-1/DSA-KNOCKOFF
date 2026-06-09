#Finding numbers greater than 10

def greater_than_10(arr):
    result = []

    for i in arr:
        if i > 10:
            result.append(i)

    return result

print(greater_than_10([3, 10, 15, 7, 25]))
#Finding the maximum number in a list

def maximum(arr):
    mx = arr[0]

    for i in arr:
        if i > mx:
            mx = i

    return mx

print(maximum([10, 20, 5, 7, 50]))
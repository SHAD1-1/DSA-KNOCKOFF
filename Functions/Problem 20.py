# Finding largest and smallest elements

def largest_smallest(arr):
    max = arr[0]
    min = arr[0]

    for i in arr:
        if i > max:
            max = i

        if i < min:
            min = i

    return min, max

min, max = largest_smallest([7, 2, 9, 4, 1])

print("Min =", min)
print("Max =", max)
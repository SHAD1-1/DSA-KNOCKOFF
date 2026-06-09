#Write a function that returns the minimum, maximum and the average value of an array passed as a parameter.

def array_stats(arr):
    minimum = arr[0]
    maximum = arr[0]
    total = 0

    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]

        if arr[i] > maximum:
            maximum = arr[i]

        total += arr[i]

    average = total / len(arr)

    return minimum, maximum, average


# Main program
arr = [7, 3, 9, 1, 5]

minimum, maximum, average = array_stats(arr)

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
#Write a function that sorts an array of numbers. In the main function, first create and print the unsorted array, then use the function to sort the array, then print the sorted array.


def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

                

    return arr


# Main part
arr = [7, 3, 9, 1, 5]

print("Unsorted array:", arr)

sort_array(arr)

print("Sorted array:", arr)
#Write a function to reverse a list

def reverse_list(arr):
    new_arr = []

    for i in range(len(arr) - 1, -1, -1):
        new_arr.append(arr[i])

    return new_arr

print(reverse_list([1, 2, 3, 4]))
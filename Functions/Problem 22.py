#Func to remove duplicates
def remove_duplicates(arr):
    new_arr = []

    for i in arr:
        found = False

        for j in new_arr:
            if i == j:
                found = True

        if found == False:
            new_arr.append(i)

    return new_arr

print(remove_duplicates([1, 2, 2, 3, 4, 4]))


def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]
def reverse_func(num):
    lst = ""

#lst = [1,2,3,4,5]
    for i in str(num):
        lst = i + lst

    return int(lst)



print(reverse_func(12345)) 
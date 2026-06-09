#Input and print a 2D List

def print_2D(num):
    for i in num:
        for j in i:
            print(j,end=" ")

        print()


    
arr = [[1,2,3],[4,5,6]]

print_2D(arr)



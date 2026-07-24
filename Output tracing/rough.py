n = 4
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i + j) % 2 == 0:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print()


    def is_palindrome(lst):
        lst = str(lst)

        if lst == lst[::-1]:
            return True

        else:
            return False
        

def is_palindromee(lst):
    last = lst[-1]

    for i in lst:
        if lst[i] == last:
            return True
        
        else:
            return False
        



        
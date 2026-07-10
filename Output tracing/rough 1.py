def is_arithmatic(lst):
    comondif = lst[0] - lst[1]
    for i in lst:
        if lst[i] - lst[i+1] == comondif:
            return True
        else:
            return False
        
    return is_arithmatic
x = [1,4,7,10,13, 2]
print(is_arithmatic(x))

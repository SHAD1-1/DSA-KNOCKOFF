def is_Arithmatic(lst):
    if len(lst) <2:
        return False
    
    diff = lst[1] -lst[0]
    for i in range(1,len(lst)-1):
        if lst[i+1] - lst[i] != diff:
            return False
        
    return True

var = [2,4,6,8,9,10]
print(is_Arithmatic(var))

def remove_duplicates(lst):
    result = []
    for num in lst:
        if num in result:   
            continue   
        else:
            result.append(num)    
    return result
lst1 = [1,1,2,3,4,4,5]
print(remove_duplicates(lst1))

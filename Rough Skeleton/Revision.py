# LST = [1,2,3,4,5,6,7,8,9,10]

def count(lst):
    count = 0
    for i in lst:
        count += 1

    return count

usage = [1,2,3,4,5,6,7,8,9,10]

print(count(usage))


def reverse(lst):
    result = []
    for i in range(len(lst)-1,-1,-1):
        result.append(lst[i])

    return result

print(reverse(usage))


def AddAll(lst):
    result = 0
    for i in lst:
        result += i


    return result

print(AddAll(usage))


def highest(lst):
    first = lst[0]
    for i in lst:
        if i > first:
            first = i

    return first

print(highest(usage))

def lowest(lst):
    first = lst[0]
    for i in lst:
        if i < first:
            first = i

    return first

print("Lowest:",lowest(usage))



def mid(lst):
    middle = len(lst) // 2
    return lst[middle]

print("Mid: ",mid(usage))


def avg(lst):
    total = 0

    for i in lst:
        total += i

    return total // len(lst)

print("Avg:",avg(usage))


def secondLargest(lst):
    lar = lst[0]
    smal = lst[0]

    for i in lst:
        if i >lar:
            smal = lar
            lar = i
        elif i > smal and i != lar:
            smal = i

        
    

    return smal

print(secondLargest(usage))





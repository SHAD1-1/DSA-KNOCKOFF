def minssquare(x):
    n = 0
    total = 0
    while total < x:
        n += 1
        total += n * n

    return n

y = 55
print(minssquare(y))

def top_students(results_list, passing_mark):
    result = ___
    for ___ in results_list:
        if ___[1] == ___ and ___[2] > ___:
            result.append(___[___])
    return ___



def top_Students(lst,pass_mark):
    result = []
    for i in lst:
        if i[1] == "A" and i[2] >= 70:
            result.append(i[0])

    return result


def shift(stk):
    # Step 1 - save top
    ___ = stk.___()
    
    # Step 2 - move all to temp
    temp = Stack()
    while not stk.___():
        temp.push(stk.___())
    
    # Step 3 - push top to bottom
    stk.push(___)
    
    # Step 4 - move back
    while not temp.___():
        stk.push(temp.___())
    
    return stk

def shift(stk):
    temp = Stack()
    while not stk.isempty():
        temp.push(stk.pop())

    stk.push()

def queue2stack(q):
    # Step 1 - temp stack
    temp = Stack()
    while not q.___():
        temp.push(q.___())
    
    # Step 2 - final stack
    final = Stack()
    while not temp.___():
        final.push(temp.___())
    
    return final

def queue2stack(q):
    temp = Stack()
    while not q.isEmpty():
        temp.push(q.dequeue())

    final = Stack()
    while not temp.isEmpty():
        final.push(temp.pop())

    return final

def sort_stack(stk):
    # Step 1 - pop all into list
    lst = []
    while not stk.___():
        lst.___(stk.___())
    
    # Step 2 - sort largest first
    lst.sort(reverse=___)
    
    # Step 3 - push back
    for num in lst:
        stk.___(num)
    
    return stk

def sort_stack(stk):
    lst = []
    while stk.isEmpty():
        lst.pop(stk.peek())

    lst.sort(reverse= True)

    for num in lst:
        stk.push(num)

    return stk




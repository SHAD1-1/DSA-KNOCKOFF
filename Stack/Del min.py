def deleteMin(stk):
    aux = Stack()
    min_val = stk.peek()

    while not stk.isEmpty():
        v = stk.pop()
        if v < min_val:
            min_val = v
        aux.push(v)

    skipped = False
    while not aux.isEmpty():
        v = aux.pop()
        if v == min_val and not skipped:
            skipped = True
            continue
        stk.push(v)

    return stk
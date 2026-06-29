def reverseK(q, k):
    # Step 1 - push first k to stack
    stk = Stack()
    for i in range(___):
        stk.push(q.___())
    
    # Step 2 - pop stack back to queue
    while not stk.___():
        q.enqueue(stk.___())
    
    # Step 3 - move remaining to back
    remaining = q.size() - ___
    for i in range(___):
        q.enqueue(q.___())
    
    return q

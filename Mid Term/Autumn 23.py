#2
def oppr(q1):
    stk = Stack()
    q3 = Queue() 

    while not q1.isEmpty():
        stk.push(q1.dequeue())

    while not stk.isEmpty():
        q3.enqueue(stk.pop())


    return q3



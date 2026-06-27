def fun(n, k):
    q = Queue()
    for i in range(n):
        q.enqueue(3 * i)
    for i in range(k):
        q.enqueue(q.peek())
        q.dequeue()
    return q.peek()
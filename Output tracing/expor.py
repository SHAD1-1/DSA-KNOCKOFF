def fun(n, k):
    q = Queue()
    for i in range(n):
        q.enqueue(3 * i)
    for i in range(k):
        q.enqueue(q.peek())
        q.dequeue()
    return q.peek()


n = 4
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i + j) % 2 == 0:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print()

 

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


def removeAdjacentDuplicates(q):
    result = Queue()
    if q.isEmpty():
        return result

    last = q.peek() #5
    result.enqueue(last)
    q.dequeue()

    while not q.isEmpty():
        current = q.dequeue()
        if current != last:
            result.enqueue(current)
            last = current

    return result


#Queue

def someFunction(self):
    current = self.head      # start at the beginning
    result = ...              # a counter, sum, or list — whatever you're building
    
    while current is not None:      # walk until you fall off the end
        # do something with current.data
        current = current.next      # ALWAYS move forward, or infinite loop!
    
    return result

def sumList(self):
    current = self.head
    total = 0         # what should this start as?
    
    while current is not None:
        total += current.data               # what do you do to total, using current.data?
        current = current.next
    
    return total

def findMax(self):
    current = self.head
    result = self.head.data     # start with the first value, not 0
    
    while current is not None:
        if current.data > result:
            result = current.data          # what goes here?
        current = current.next            # what goes here? (same as always)
    
    return result


#####

def isEqual(q1, q2):
    aux1 = Queue()## [1,2,3,4,5]
    aux2 = Queue()
    equal = True
    
    if q1.size() != q2.size():
        equal = False
    
    while not q1.isEmpty() and not q2.isEmpty():
        v1 = q1.dequeue()  ##
        v2 = q2.dequeue()
        
        if v1 != v2:
            equal = False
        
        aux1.enqueue(v1)
        aux2.enqueue(v2)
    
    while not aux1.isEmpty():
        q1.enqueue(aux1.dequeue())
    
    while not aux2.isEmpty():
        q2.enqueue(aux2.dequeue())
        
    return equal


def reverseK(q,k):
    aux = Stack()

    for i in range(k):
        aux.push(q.dequeue())

    while not aux.isEmpty():
        q.enqueue(aux.pop())


    for i in range(q.size()-k):
        q.enqueue(q.dequeue())

    return q

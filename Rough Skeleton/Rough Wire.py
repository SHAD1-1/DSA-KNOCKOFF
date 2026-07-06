def queue(q1,q2):
    aux1 = Queue()  #[1,2,3,4,5]
    aux2 = Queue()  #[1,2,3,4,5]
    equal = True

    if q1.size != q2.size:
        equal = False

    while not q1.isEmpty and not q2.isEmpty:
        v1 = q1.dequeue()  #[1,2,3,4,5]
        v2 = q2.dequeue()  #[1,2,3,4,5]

        if v1 != v2:
            equal = False

        aux1.enqueue(v1) #[1,2,3,4,5]
        aux2.enqueue(v2)

    while not aux1 isEmpty:
        q1.enqueue(aux1)  #[1,2,3,4,5]
    
    while not aux2 isEmpty:
        q1.enqueue(aux2)

    return equal




    

    
def queue(q1,q2):
    aux1 = Queue()  #[1,2,3,4,5]
    aux2 = Queue()  #[1,2,3,4,5]
    count = 0


    while not q1.isEmpty() and not q2.isEmpty():
        v1 = q1.dequeue()  #[1,2,3,4,5]
        v2 = q2.dequeue()  #[1,2,3,4,5]

        if v1 != v2:
            count += 1

        aux1.enqueue(v1) #[1,2,3,4,5]
        aux2.enqueue(v2)

    while not aux1.isEmpty():
        q1.enqueue(aux1)  #[1,2,3,4,5]
    
    while not aux2.isEmpty():
        q1.enqueue(aux2)
        

    return count




    

    

    




    




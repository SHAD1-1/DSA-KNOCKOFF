def delete(lst): #1,2,3,4,5,14,6
    aux = Stack()
    max = lst.peek()

    while not lst.isEmpty():
        v = lst.pop()
        if v > max:
            max = v

        aux.push(v)

    
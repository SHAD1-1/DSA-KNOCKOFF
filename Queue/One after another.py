def interleave(q): #[1,2,3,4,5,6]
    half = q.size() // 2   #[3]
    
    # Step 1 - first half into stack1
    stk1 = Stack() ##[3,2,1]
    for i in range(half): #[3]
        stk1.push(q.dequeue())  
    
    # Step 2 - second half into stack2
    stk2 = Stack()
    for i in range(half):        # ✅ half not empty
        stk2.push(q.dequeue())  #[3,2,1]
    
    # Step 3 - reverse stk1 into temp1
    temp1 = Stack() #[1,2,3]
    while not stk1.isEmpty():   # ✅ isEmpty
        temp1.push(stk1.pop())  # ✅ pop #
    
    # Step 4 - reverse stk2 into temp2
    temp2 = Stack() #[4,5,6]
    while not stk2.isEmpty():   # ✅ isEmpty
        temp2.push(stk2.pop())  # ✅ pop
    
    # Step 5 - enqueue alternately
    while not temp1.isEmpty():  # ✅ isEmpty #[1,2,3]
        q.enqueue(temp1.pop())  # ✅ pop #[3,2,1] after pop enq = []
        q.enqueue(temp2.pop())  # ✅ pop
    
    return q
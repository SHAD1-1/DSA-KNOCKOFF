sll.head = Node(40)

for elem in lst:
    nd = Node(elem)
    if elem > sll.head.data:
        nd.next = sll.head
        sll.head = nd
    else:
        nd.next = sll.head.next
        sll.head.next = nd
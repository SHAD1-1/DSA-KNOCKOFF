#Focus on the functions and class node is just built in.

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

# Create nodes
head = Node(5)
head.next = Node(6)
head.next.next = Node(7)
head.next.next.next = Node(8)
def getAverage(head):
    if head is None:
        return 0

    total = 0
    count = 0
    lst = head

    while lst:
        total += lst.data
        count += 1
        lst = lst.next

    return total / count

print(getAverage(head))
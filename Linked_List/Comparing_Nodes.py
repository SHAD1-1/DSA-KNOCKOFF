#Comparing if the two Singly Linked List are equal or not

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def compare_lists(head1, head2):
    current1 = head1
    current2 = head2

    while current1 is not None and current2 is not None:
        if current1.data != current2.data:
            return False

        current1 = current1.next
        current2 = current2.next

    return current1 is None and current2 is None


# List A: 7 -> 6 -> 10 -> 11
A = Node(7)
A.next = Node(6)
A.next.next = Node(10)
A.next.next.next = Node(11)

# List B: 7 -> 6 -> 10 -> 11
B = Node(7)
B.next = Node(6)
B.next.next = Node(10)
B.next.next.next = Node(11)

# List C: 7 -> 16 -> 10 -> 11
C = Node(7)
C.next = Node(16)
C.next.next = Node(10)
C.next.next.next = Node(11)

print("A and B are equal:", compare_lists(A, B))
print("A and C are equal:", compare_lists(A, C))
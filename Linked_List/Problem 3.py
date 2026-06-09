class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(5)
head.next = Node(10)
head.next.next = Node(15)

def equalNode(head1, head2):

    while head1 and head2:

        if head1.data != head2.data:
            return False

        head1 = head1.next
        head2 = head2.next

    return head1 is None and head2 is None
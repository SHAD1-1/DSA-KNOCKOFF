class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly:
    def __init__(self):
        self.head = None

    def reverseList(self):
        prev = None
        current = self.head

        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        self.head = prev

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end=" ")
            current = current.next

        print()


sll = Singly()

sll.head = Node(3)
sll.head.next = Node(10)
sll.head.next.next = Node(17)
sll.head.next.next.next = Node(61)
sll.head.next.next.next.next = Node(107)

print("Original List:")
sll.display()

sll.reverseList()

print("Reversed List:")
sll.display()
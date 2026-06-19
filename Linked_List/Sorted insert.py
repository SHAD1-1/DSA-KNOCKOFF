class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Singly:
    def __init__(self):
        self.head = None

    def sort(self, value):
        newNode = Node(value)

        if self.head is None or value < self.head.data:
            newNode.next = self.head
            self.head = newNode
            return

        current = self.head

        while current.next != None and current.next.data < value:
            current = current.next

        newNode.next = current.next
        current.next = newNode

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end=" ")
            current = current.next

        print()


sll = Singly()

sll.head = Node(2)
sll.head.next = Node(3)
sll.head.next.next = Node(4)
sll.head.next.next.next = Node(6)

print("Before:")
sll.display()

sll.sort(5)
sll.sort(1)


print("After:")
sll.display()
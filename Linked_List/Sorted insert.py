class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, v):
        newNode = Node(v)

        # Insert at the beginning
        if self.head is None or v < self.head.data:
            newNode.next = self.head
            self.head = newNode
            return

        temp = self.head

        while temp.next != None and temp.next.data < v:
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode

    def display(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Create list: 3 -> 6 -> 7 -> 10
sll = SinglyLinkedList()

sll.head = Node(3)
sll.head.next = Node(6)
sll.head.next.next = Node(7)
sll.head.next.next.next = Node(10)

print("Before insertion:")
sll.display()

sll.sorted_insert(5)

print("After insertion:")
sll.display()
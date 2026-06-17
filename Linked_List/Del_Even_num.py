#Deleting the even numbers in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def deleteEven(self):

        # Remove even nodes from the beginning
        while self.head is not None and self.head.data % 2 == 0:
            self.head = self.head.next

        current = self.head

        while current is not None and current.next is not None:

            if current.next.data % 2 == 0:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create List A
sll = SinglyLinkedList()

sll.append(2)
sll.append(5)
sll.append(8)
sll.append(7)
sll.append(10)
sll.append(11)
sll.append(12)

print("Before deleting even numbers:")

sll.display()

sll.deleteEven()

print("After deleting even numbers:")
sll.display()
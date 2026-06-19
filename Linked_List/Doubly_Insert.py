class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end (for creating the list)
    def addLast(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode
        newNode.prev = current

    # Insert after a given value
    def addNodeAfterValue(self, givenValue, newValue):
        current = self.head

        # Search for givenValue
        while current is not None:
            if current.data == givenValue:
                break
            current = current.next

        # If value not found
        if current is None:
            print("Not found")
            return

        # Create new node
        newNode = Node(newValue)

        # Connect new node
        newNode.next = current.next
        newNode.prev = current

        # Fix next node's prev link
        if current.next is not None:
            current.next.prev = newNode

        current.next = newNode

    # Display the list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


# Driver Code
dll = DoublyLinkedList()

dll.addLast(10)
dll.addLast(20)
dll.addLast(30)
dll.addLast(40)

print("Original List:")
dll.display()

dll.addNodeAfterValue(20, 25)

print("After Insertion:")
dll.display()

dll.addNodeAfterValue(50, 60)
class Node:
    def __init__(self, data):
        self.data = data      # Store the value
        self.next = None      # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None      # Initially the list is empty

    # Add a new node at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Display the linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create a linked list
ll = LinkedList()

# Insert values
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

# Display the list
ll.display()
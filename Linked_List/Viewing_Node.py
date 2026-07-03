class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = Node(20)

# Display the linked list
current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
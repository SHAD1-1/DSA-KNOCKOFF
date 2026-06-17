class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        


def addNodeBeforeValue(head, givenValue, newValue):
    newNode = Node(newValue)

    # If the given value is at the head
    if head is not None and head.data == givenValue:
        newNode.next = head
        return newNode

    prev = None
    current = head

    while current is not None:
        if current.data == givenValue:
            prev.next = newNode
            newNode.next = current
            return head

        prev = current
        current = current.next

    print("Not found")
    return head


# Create linked list: 5 -> 10 -> 15 -> 20
head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = Node(20)

# Insert 12 before 15
head = addNodeBeforeValue(head, 15, 12)

# Display the linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
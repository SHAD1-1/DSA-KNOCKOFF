class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def find_maximum(self):
        if self.head is None:
            return None

        max_value = self.head.data
        current = self.head.next

        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


# --- Let's test it out ---

my_list = LinkedList()

my_list.append(10)
my_list.append(45)
my_list.append(3)
my_list.append(78)
my_list.append(22)
my_list.append(91)
my_list.append(5)

print("Linked List:")
my_list.display()

maximum = my_list.find_maximum()
print(f"\nMaximum value in the list: {maximum}")
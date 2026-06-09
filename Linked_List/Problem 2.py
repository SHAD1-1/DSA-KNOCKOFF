# 1. Define the Node structure for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def numOfOccurrences(head, data):
    count = 0
    temp = head

    while temp:
        if temp.data == data:  
            count += 1
        temp = temp.next 
        
    return count



head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

# Finding occurrences of the number 1
target = 1
result = numOfOccurrences(head, target)

print(f"The number {target} appears {result} times in the linked list.")
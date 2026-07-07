# Stack Class
class Stack:
    def __init__(self):
        self.items = []

    # Push an element onto the stack
    def push(self, item):
        self.items.append(item)

    # Remove and return the top element
    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    # Return the top element without removing it
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    # Check if the stack is empty
    def isEmpty(self):
        return len(self.items) == 0

    # Return the size of the stack
    def size(self):
        return len(self.items)

    # Display the stack
    def display(self):
        print(self.items)


# Function to delete the minimum value from the stack
def deleteMin(stk):
    aux = Stack()
    min_val = stk.peek()

    # Find the minimum value
    while not stk.isEmpty():
        v = stk.pop()
        if v < min_val:
            min_val = v
        aux.push(v)

    # Restore the stack, skipping the first occurrence of the minimum
    skipped = False
    while not aux.isEmpty():
        v = aux.pop()
        if v == min_val and not skipped:
            skipped = True
            continue
        stk.push(v)

    return stk


# ---------------- Example Usage ----------------

stk = Stack()

# Push elements
stk.push(8)
stk.push(3)
stk.push(10)
stk.push(1)
stk.push(6)
stk.push(1)   # Duplicate minimum value

print("Original Stack:")
stk.display()

deleteMin(stk)

print("Stack after deleting the first minimum value:")
stk.display()
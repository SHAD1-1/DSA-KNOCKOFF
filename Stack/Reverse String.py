class Stack:
    def __init__(self):
        self.items = []
        #Radwan

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def isEmpty(self):
        return len(self.items) == 0



stack = Stack()

text = input("Enter a string: ")

for ch in text:
    stack.push(ch)

print("\nReversed String:")
while not stack.isEmpty():
    ch = stack.pop()
    print(ch, end=" ")

print("\n\nCharacters and their Unicode values:")

for ch in text:
    stack.push(ch)

while not stack.isEmpty():
    ch = stack.pop()
    print(ch, "->", ord(ch))
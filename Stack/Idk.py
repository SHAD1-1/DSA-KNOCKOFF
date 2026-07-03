class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None


lst = [4, 7, 2, 9, 1, 6, 3]
stk = Stack()

for elem in lst:
    if stk.isEmpty() or elem > stk.peek():
        stk.push(elem)

result = []
while not stk.isEmpty():
    result.append(stk.pop())

print(result)
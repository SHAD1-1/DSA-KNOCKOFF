# ==========================================================
# TRACE TABLE TEMPLATE
# ==========================================================

"""
| Step | var1 | var2 | ... | condition | output/action |
|------|------|------|-----|-----------|---------------|
| 1    |      |      |     |           |               |
| 2    |      |      |     |           |               |
| 3    |      |      |     |           |               |

Rule:
- One row per step.
- Never skip a step.
"""


# ==========================================================
# BOOLEAN CHECK TEMPLATE
# ==========================================================

def isX(lst):
    if len(lst) <= 1:
        return True

    for i in range(len(lst) - 1):
        if False:      # Replace with condition that breaks the property
            return False

    return True


# ==========================================================
# SINGLY LINKED LIST — WALK & COMPUTE
# ==========================================================

def someFunction(self):
    current = self.head
    result = 0          # Change starting value

    while current is not None:
        # Update result using current.data
        current = current.next

    return result


# ==========================================================
# SINGLY LINKED LIST — INSERT RELATIVE TO FOUND NODE
# ==========================================================

def insertRelated(self, data):
    new_node = Node(data)

    prev = None
    current = self.head

    target_prev = None
    target = self.head

    while current is not None:

        if False:       # Replace with target condition
            target = current
            target_prev = prev

        prev = current
        current = current.next

    if target_prev is None:
        new_node.next = self.head
        self.head = new_node
    else:
        new_node.next = target
        target_prev.next = new_node


# ==========================================================
# DOUBLY LINKED LIST — INSERT TEMPLATE
# ==========================================================

def insertBetween(left_neighbor, right_neighbor, new_node):

    # Always fix FOUR links

    new_node.prev = left_neighbor
    new_node.next = right_neighbor

    left_neighbor.next = new_node
    right_neighbor.prev = new_node


# ==========================================================
# DOUBLY LINKED LIST — FRONT/BACK SCAN
# ==========================================================

def scanFromBothEnds(self):

    front = self.head
    back = self.tail

    result = True       # Change as needed

    while (
        front is not None
        and back is not None
        and front != back
        and front.next != back
    ):

        # Compare front.data and back.data
        # OR update result

        front = front.next
        back = back.prev

    return result


# ==========================================================
# STACK PATTERN A
# Drain → Track → Rebuild
# ==========================================================

def someFunction(original):

    aux = Stack()

    while not original.isEmpty():

        v = original.pop()

        # Update tracker or decide to skip

        aux.push(v)

    while not aux.isEmpty():

        v = aux.pop()

        # Apply real logic

        original.push(v)

    return original


# ==========================================================
# STACK / QUEUE PATTERN B
# Compare two structures
# ==========================================================

def compareStructures(a, b):

    auxA = Queue()
    auxB = Queue()

    result = True

    while not a.isEmpty() and not b.isEmpty():

        va = a.dequeue()
        vb = b.dequeue()

        # Compare va and vb
        # Update result
        # NEVER return early

        auxA.enqueue(va)
        auxB.enqueue(vb)

    while not auxA.isEmpty():
        a.enqueue(auxA.dequeue())

    while not auxB.isEmpty():
        b.enqueue(auxB.dequeue())

    return result


# ==========================================================
# STACK PATTERN C
# Balanced Brackets
# ==========================================================

def isBalanced(s):

    stk = Stack()

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        if ch in "({[":
            stk.push(ch)

        elif ch in ")}]":

            if stk.isEmpty():
                return False

            if stk.peek() == pairs[ch]:
                stk.pop()
            else:
                return False

    return stk.isEmpty()


# ==========================================================
# STACK / QUEUE PATTERN D
# Reverse first k elements
# ==========================================================

def reverseK(q, k):

    aux = Stack()

    for _ in range(k):
        aux.push(q.dequeue())

    while not aux.isEmpty():
        q.enqueue(aux.pop())

    for _ in range(q.size() - k):
        q.enqueue(q.dequeue())

    return q


# ==========================================================
# STACK / QUEUE PATTERN E
# Move between containers
# ==========================================================

"""
pop A -> push B

pop B -> push C

Two reversals
Same order as original


pop A -> push B

One reversal
Reverse order
"""


# ==========================================================
# 2D LIST TEMPLATE
# ==========================================================

for row in range(len(matrix)):

    for col in range(len(matrix[row])):

        val = matrix[row][col]

        # Use val


# -------------------------
# Row sums
# -------------------------

for row in range(len(matrix)):

    row_sum = 0

    for col in range(len(matrix[row])):
        row_sum += matrix[row][col]

    print(row_sum)


# -------------------------
# Column sums
# -------------------------

num_cols = len(matrix[0])

col_sums = [0] * num_cols

for row in range(len(matrix)):
    for col in range(num_cols):
        col_sums[col] += matrix[row][col]


# -------------------------
# Main diagonal
# -------------------------

diag_sum = 0

for i in range(len(matrix)):
    diag_sum += matrix[i][i]


# ==========================================================
# 1D LIST TEMPLATE
# ==========================================================

def scanList(A):

    best = A[0]

    for val in A:

        # Update best

        pass

    return best


# ==========================================================
# SECOND LARGEST
# ==========================================================

def secondLargest(A):

    largest = float("-inf")
    second = float("-inf")

    for val in A:

        if val > largest:

            second = largest
            largest = val

        elif largest > val > second:

            second = val

    return second


# ==========================================================
# POINTER HOP COUNTING NOTES
# ==========================================================

"""
Pointer-Hop Rules

1.
Count the number of .next on the LEFT side.

2.
Drop the LAST .next.

3.
Move that many hops from head.

That node's .next is modified.

4.
On the RIGHT side,
count ALL .next hops.

5.
Everything else in the list
stays unchanged unless reassigned.
"""
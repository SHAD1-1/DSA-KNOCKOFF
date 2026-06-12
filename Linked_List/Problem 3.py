
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

# Create nodes
head = Node(5)
head.next = Node(6)
head.next.next = Node(7)
head.next.next.next = Node(8)




def is_identical(list1, list2):
  identical = True
  if list1.size!=list2.size:
    return False
  else:
    if list1.size!=0 and list2.size!=0:
      current_node1 = list1.head
      current_node2 = list2.head

      while current_node1 is not None:
        if current_node1.data == current_node2.data:
          identical = True
        else:
          identical = False
          return identical
        current_node1 = current_node1.next
        current_node2 = current_node2.next

  return identical

s1 = SinglyLinkedList()
s1.append(10)
s1.append(40)
s1.append(30)
s2 = SinglyLinkedList()
s2.append(10)
s2.append(80)
s2.append(30)
print(is_identical(s1,s2))

s3 = SinglyLinkedList()
s3.append(10)
s3.append(40)
s3.append(30)
s4 = SinglyLinkedList()
s4.append(10)
s4.append(40)
s4.append(30)
print(is_identical(s3,s4))
class Student:
    
    def __init__(self, student_id, name,id,courses):
        self.student_id = student_id
        self.name = name
        self.id = id
        self.courses = self.courses

        self.next = None

    def print_name()


s1 = Student(101, "Alice")
s2 = Student(102, "Bob")
s3 = Student(103, "Charlie")

# Link the nodes
s1.next = s2
s2.next = s3


current = s1

while current is not None:
    print("ID:", current.student_id)
    print("Name:", current.name)
    print()
    current = current.next
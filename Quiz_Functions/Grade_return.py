
students = [
    [1234111, 65],
    [1234222, -1],
    [1234333, -1],
    [1234444, 85],
    [1234555, 35]
]

def get_grade(mark):
    if mark >= 80 and mark <= 100:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"
    

for student in students:
    student_id = student[0]
    mark = student[1]

    if mark == -1:
        print(student_id, "W")
    else:
        print(student_id, get_grade(mark))


#Removing withdrawn students
new_list = []

for student in students:
    if student[1] != -1:
        new_list.append(student)

for student in new_list:
    print(student[0], get_grade(student[1]))
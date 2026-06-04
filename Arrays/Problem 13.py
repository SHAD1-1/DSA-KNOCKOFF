#Create a 5 x 3 integer array. Fill it with random numbers between 30 and 50. Print the array.
import random
arr = []
for i in range(5):
    row = []
    for j in range(3):
        row.append(random.randint(30, 50))
    arr.append(row)
print("Array:")
for row in arr:
    print(row)


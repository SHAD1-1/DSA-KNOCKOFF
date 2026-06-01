size = int(input("Enter the size of the array: "))

arr = []

a = 0
b = 1

for i in range(size):
    arr.append(a)
    
    next_num = a + b
    a = b
    b = next_num

print("Fibonacci Array:", arr)
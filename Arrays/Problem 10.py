size = int(input("Enter the size: "))
arr = []

for i in range(size):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
#[1, 2, 3, 4, 5]
count = 0

for i in arr: 
    if i > 1:
        is_prime = True 

        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

print("Array:", arr)
print("Number of prime numbers:", count)


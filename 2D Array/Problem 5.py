# Count the number of prime numbers in a 2D array.
arr = [
    [2, 4, 7],
    [10, 13, 15],
    [17, 20, 23]
]

count = 0

for row in arr:
    for num in row:

        prime = True

        if num < 2:
            prime = False

        for i in range(2, num):
            if num % i == 0:
                prime = False

        if prime:
            count += 1

print("Number of prime numbers:", count)
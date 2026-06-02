size = int(input("Enter array size: "))

arr = []

# Take input
for i in range(size):
    num = int(input("Enter a number: "))
    arr.append(num)

# Count occurrences
for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    print(arr[i], "occurs", count, "times")
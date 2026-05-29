# Create an integer array of size 10
arr = []

# Take input from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("Array:", arr)

# Assume the array is sorted both ways at first
ascending = True
descending = True

# Check sorting
for i in range(len(arr) - 1):

    # Check ascending
    if arr[i] > arr[i + 1]:
        ascending = False

    # Check descending
    if arr[i] < arr[i + 1]:
        descending = False

# Print result
if ascending:
    print("The array is sorted in ascending order.")

elif descending:
    print("The array is sorted in descending order.")

else:
    print("The array is not sorted.")
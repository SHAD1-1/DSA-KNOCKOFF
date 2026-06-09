#Write a function to check if a number is a perfect number.
def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        return True
    else:
        return False


print(is_perfect(6))   # True
print(is_perfect(12))  # False
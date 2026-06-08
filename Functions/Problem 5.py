#Write a func that includes am integer as parameter and returns the sum in that list.
def sum_digits(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total

# Example
print(sum_digits(12345))
#Write a function that takes an integer as parameter and returns the number of digits.

def count_int(num):

    count = 0

    for i in str(num):
        count += 1

    return count

print(count_int(1234292215))


def count_while(num1):
    count = 0

    while num1 > 0:
        count += 1
        num1 = num1 // 10
    return count

print(count_while(12345678))
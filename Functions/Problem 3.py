#Write a function that takes a number as parameter and returns the factorial.

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

# Example
print(factorial(5))
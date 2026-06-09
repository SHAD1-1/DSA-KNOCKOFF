#Write a function that takes two numbers as parameters and returns their LCM.
def lcm(num1,num2):
    gcd = 1

    smaller = num1

    if num2 < num1:
        smaller = num2

    for i in range(1,smaller +1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    return (num1 * num2) // gcd\
    


print(lcm(12,18))

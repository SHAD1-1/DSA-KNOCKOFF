#Write a function that takes a number and a character (as parameters) and prints a triangle of that size using the specified character.

def triangle(size, ch):
    for i in range(1, size + 1):
        return ch * i
    

# Example
print(triangle(5, "*"))

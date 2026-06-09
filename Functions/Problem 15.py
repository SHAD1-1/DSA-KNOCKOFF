#. Write a function that takes a string as a parameter, changes all the letters to uppercase letters and returns the updated string.

def to_uppercase(num):
    result = ""

    for i in range(len(num)):
        char = num[i]

        if "a" <= char <= "z":
            result += chr(ord(char) - 32)

        else:
            result += char

    
    return result


num = "I love programming"

print("Original: ", num)
print("Uppercase: ", to_uppercase(num))

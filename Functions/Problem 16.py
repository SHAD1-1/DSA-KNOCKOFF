#Write a function that takes an IUB student ID as a string parameter, then checks if the ID is valid. If the ID is valid the function returns true, otherwise it returns false.

def check_id(num):
    if len(num) != 7:
        return False
    
    for i in num:
        if i < "0" or i > "9":
            return False
        

    return True


my_id = "2310421"

print("Valid",check_id(my_id))

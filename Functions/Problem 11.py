#Write a func to see if a number is palindrome

def is_palindrome(num1):
    lst = str(num1)
    reverse = ''
      #lst = [1234]
    for i in range(len(lst)-1,-1,-1):
        reverse = reverse + lst[i]


    if lst == reverse:
        return True
    
    else:
        return False
    

print(is_palindrome(121))


#Write a function that takes a string as parameter and returns the number of words in that string.

def count_words(num):
    count = 0 
    word = False

    for i in range(len(num)):
        if num[i] != " " and word == False:
            count += 1
            word = True

        elif num[i] == " ":
            word = False
    return count


num = "I work hard"

print("String: ",num)

print("Number of words: ", count_words(num))

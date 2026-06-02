num = int(input("Enter a decimal number: "))

binary = ""

for i in range(20):


    if num == 0:
        break
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary:", binary)








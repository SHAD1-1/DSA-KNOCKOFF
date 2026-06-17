def print_triangle(num, ch):

    for i in range(1, num + 1):
        for j in range(i):
            print(ch, end="")
        print()

print_triangle(5, "*")



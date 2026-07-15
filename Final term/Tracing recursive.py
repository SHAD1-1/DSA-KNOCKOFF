def count_down(n):
    if n > 3:
        return
    count_down(n + 1)
    print(n)

count_down(1)

print()
print()


def rec(n):
    if n >= 10:
        return
    rec(n + 2)
    print(n, end=' ')
    rec(n + 1)


rec(6)

def rec(n):
    if n >= 10:
        return
    rec(n + 2)
    print(n, end=' ')
    rec(n + 1)
    

rec(6)
def minssquare(x):
    n = 0
    total = 0
    while total < x:
        n += 1
        total += n * n

    return n

y = 55
print(minssquare(y))

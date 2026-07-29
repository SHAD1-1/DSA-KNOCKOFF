def rec(n):
    if n >= 10: return
    rec(n + 2)
    print(n, end=' ')
    rec(n + 1)

rec(6)

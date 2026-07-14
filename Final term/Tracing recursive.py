def count_down(n):
    if n > 3:
        return
    count_down(n + 1)
    print(n)

count_down(1)

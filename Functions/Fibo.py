def fibo(n):
    if n <= 2:
        result = 1

    else:
        result = fibo(n-1) + fibo(n-2)

    return result

print(fibo(8))        



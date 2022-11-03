known = {0: 0, 1: 1}

def fibonacci(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

print(fibonacci(10))

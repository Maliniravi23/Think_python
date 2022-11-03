m = int(input("Enter m \n"))
n = int(input("Enter n \n"))

def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

result = ack(m,n)
print(result)
known = {}

def ackermann(m, n):
    if m in known:
        return known[m]
    
    if n in known:
        return known[n]
    
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3, 4))

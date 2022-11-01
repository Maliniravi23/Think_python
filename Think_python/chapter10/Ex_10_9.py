def remove_duplicates(t):
    x = []
    for a in t:
        if a not in x:
            x.append(a)
    return x

t = [1,24,3,6,8,42,2,1,1,8]
print(remove_duplicates(t))
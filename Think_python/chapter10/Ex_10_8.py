def has_duplicates(t):
    i = 0
    while i < len(t) - 1:
        if t[i] == t[i + 1]:
            return True
        i += 1
    return False
        

t = [1,2,3,4,5]
print(has_duplicates(t))
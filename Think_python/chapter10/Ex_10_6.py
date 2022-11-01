def is_sorted(t):
    if t == sorted(t):
        return True
    return False

t=[1,2,34,6]
print(is_sorted(t))
s=['a','b','c']
print(is_sorted(s))
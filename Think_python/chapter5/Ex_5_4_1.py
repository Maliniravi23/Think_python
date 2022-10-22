def is_triangle(a, b, c):
    if a >= b and a >= c:
        greater = a
        short1, short2 = b, c
    elif b >= c and b >= a:
        greater = b
        short1, short2 = a, c
    else:
        greater = c
        short1, short2 = a, b
    if greater > short1 + short2:
        print("No.")
    else:
        print("Yes.")
    
is_triangle(3, 7, 3)
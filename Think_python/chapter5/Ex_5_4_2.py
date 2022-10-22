from termios import B50


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
    
def get_triangle():
    a = input("What is the length of the first stick?\n")
    b = input("What is the length of the second stick?\n")
    c = input("What is the length of the third stick?\n")
    print("\n")
    is_triangle(int(a), int(b), int(c))

get_triangle()

def check_fermat(a, b, c, n):
    if n <= 2:
        print("Fermat's theorem only works for exponents larger than two.")
    elif a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        
def input_fermat():
    a = input("What is the value of 'a'?\n")
    b = input("What is the value of 'b'?\n")
    c = input("What is the value of 'c'?\n")
    n = input("What is the value of 'n'?\n")
    print("\n")
    return check_fermat(int(a), int(b), int(c), int(n))

input_fermat()

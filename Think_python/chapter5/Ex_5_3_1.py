def check_fermat(a, b, c, n):
    if n <= 2:
        print("Fermat's theorem only works for exponents larger than two.")
    elif a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

check_fermat(8,9,4,3)
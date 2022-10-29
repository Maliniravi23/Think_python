import math

def hypotenuse(a, b):
    a2 = a**2
    b2 = b**2
    return math.sqrt(a2 + b2)

result = hypotenuse(5,6)
print("Hypotenuse of right triangle ",result)
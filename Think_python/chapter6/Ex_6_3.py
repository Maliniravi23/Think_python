x = input("Enter x \n")
y = input("Enter y \n")
z = input("Enter z \n")

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

result = is_between(x,y,z)
print(result)


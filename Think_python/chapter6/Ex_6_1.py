x = int(input("Enter value of x \n"))
y = int(input("Enter value of y \n"))

def func (x, y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

result = func(x,y)
print("Campre of x and y is ",result)
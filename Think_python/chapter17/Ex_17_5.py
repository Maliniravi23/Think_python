class Point:
    
    def __init__(self, x = 0, y = 0):
        
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({:g}, {:g})'.format(self.x, self.y)
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            return "can't add a object"

point1 = Point(46, 0)
point2 = Point(0, 10)
print(point1 + point2)
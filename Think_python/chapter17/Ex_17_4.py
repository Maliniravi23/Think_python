class Point:
    
    def __init__(self, x = 0, y = 0):
        
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({:g}, {:g})'.format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
point1 = Point(65, 0)
point2 = Point(19, 10)
print(point1 + point2)
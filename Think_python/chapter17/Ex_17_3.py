class Point:
    
    def __init__(self, x = 0, y = 0):
        
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({:g}, {:g})'.format(self.x, self.y)

point = Point(65)
print(point)
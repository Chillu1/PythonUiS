import math

class Circle():
    """
    Base circle class 
    """
    position_x : float
    position_y : float
    radius : float

    def __init__(self, position_x, position_y, radius):
        self.move(position_x, position_y)
        self.radius = radius

    def move(self, delta_x, delta_y): 
        self.position_x = delta_x
        self.position_y = delta_y
    
    def area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)

    def distance(self, other_circle):
        return round(math.sqrt((self.position_x - other_circle.position_x)**2 + (self.position_y - other_circle.position_y)**2), 2)

    def overlap(self, other_circle):
        return self.distance(other_circle) <= (self.radius + other_circle.radius)

    def __str__(self):
        return "X: {0}, Y: {1}, Radius: {2}".format(self.position_x, self.position_y, self.radius)

    def __eq__(self, otherCircle):
        return self.position_x == otherCircle.position_x and self.position_y == otherCircle.position_y and self.radius == otherCircle.radius

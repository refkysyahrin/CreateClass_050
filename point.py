from math import *

class Point:
    x = 0
    y = 0

    def set_location(self, x, y):
        self.x = 10
        self.y = 5

    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)
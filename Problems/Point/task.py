class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

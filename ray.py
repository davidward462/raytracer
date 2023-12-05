class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        self.depth = 0

    def SetDepth(self, depth):
        self.depth = depth

    def Depth(self):
        return self.depth

    def Origin(self):
        return self.origin

    def SetOrigin(self, origin):
        self.origin = origin

    def Direction(self):
        return self.direction

    def SetDirection(self, direction):
        self.direction = direction

    def __str__(self):
        return f" origin: {self.origin}\ndepth: {self.depth}\ndirection: {self.direction}"

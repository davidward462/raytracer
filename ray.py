class Ray:
    def __init__(self, origin):
        self.origin = origin
        self.depth = 0

    def SetDepth(self, depth):
        self.depth = depth

    def GetDepth(self):
        return self.depth

    def __str__(self):
        return f" origin: {self.origin}\ndepth: {self.depth}"
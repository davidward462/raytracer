class Ray:
    def __init__(self, origin):
        self.origin = origin
        self.depth = 0

    def SetDepth(self, depth):
        self.depth = depth

    def __str__(self):
        return f"origin: {self.origin}"
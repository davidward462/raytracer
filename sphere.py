class Sphere:
    def __init__(self, name):
        self.name = name
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.scaleX = 0
        self.scaleY = 0
        self.scaleZ = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.ka = 0
        self.kd = 0
        self.ks = 0
        self.kr = 0
        self.n = 0

    def __str__(self):
        return f"{self.name}\n{self.posX}"
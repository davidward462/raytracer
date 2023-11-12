class Sphere:
    def __init__(self, name, attributeList):
        self.name = name
        self.attributeList = attributeList
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

    def Parse(self):
        return 0

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.scaleX} {self.scaleY} {self.scaleZ} {self.r} {self.g} {self.b} {self.ka} {self.kd} {self.ks} {self.kr} {self.n}"

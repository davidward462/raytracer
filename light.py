class Light:
    def __init__(self, name):
        self.name = name
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.ir = 0
        self.ig = 0
        self.ib = 0

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.ir} {self.ig} {self.ib}"

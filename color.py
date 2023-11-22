import numpy as np

class Color:
    def __init__(self, r=0, g=0, b=0):
        self.value = np.array([r, g, b])

    def SetRGB(self, r ,g ,b):
        self.value[0] = r
        self.value[1] = g
        self.value[2] = b

    def Red(self):
        return self.value[0]

    def Green(self):
        return self.value[1]

    def Blue(self):
        return self.value[2]

    def AddColor(self, inColor):
        self.value = self.value + inColor.value
        
    def __str__(self):
        return f"rgb({self.value[0]}, {self.value[1]}, {self.value[2]})"

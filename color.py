import numpy as np

class Color:
    def __init__(self, r=0, g=0, b=0):
        self.rgb = np.array([r, g, b])

    def SetRGB(self, r ,g ,b):
        self.rgb[0] = r
        self.rgb[1] = g
        self.rgb[2] = b

    def Red(self):
        return self.rgb[0]

    def Green(self):
        return self.rgb[1]

    def Blue(self):
        return self.rgb[2]

    def AddColor(self, inColor):
        self.SetRGB(inColor.rgb[0], inColor.rgb[1], inColor.rgb[2])
        
    def __str__(self):
        return f"rgb({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})"
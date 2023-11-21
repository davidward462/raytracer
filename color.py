import numpy as np

class Color:
    def __init__(self, r=0, g=0, b=0):
        self.rgb = np.array([r, g, b])
        self.r = r
        self.g = g
        self.b = b
        self.value = (self.r, self.g, self.b)

    def SetValue(self, value):
        self.value = value

    def GetValue(self):
        return self.value

    def SetRGB(self, r ,g ,b):
        self.r = r
        self.g = g
        self.b = b
        self.rgb[0] = r
        self.rgb[1] = g
        self.rgb[2] = b

    def AddColor(self, inColor):
        sumR = self.r + inColor.r
        sumG = self.g + inColor.g
        sumB = self.b + inColor.b
        self.SetRGB(sumR, sumG, sumB)
        
    def __str__(self):
        return f"rgb({self.r}, {self.g}, {self.b})"
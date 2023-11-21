class Color:
    def __init__(self, r=0, g=0, b=0):
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
        
    def __str__(self):
        return f" rgb({self.r}, {self.g}, {self.b})"
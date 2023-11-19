class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.value = (r, g, b)

    def SetValue(self, value):
        self.value = value

    def GetValue(self):
        return self.value
        
    def __str__(self):
        return f" rgb({self.value})"
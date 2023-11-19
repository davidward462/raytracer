class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.value = (r, g, b)
        
    def __str__(self):
        return f" rgb({self.value})"
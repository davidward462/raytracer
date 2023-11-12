class Sphere:
    def __init__(self, attributeString):
        self.attributeString = attributeString
        self.attributeList = []
    
        # attributes for calculations
        self.name = ""
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

        self.attributeCount = 15
        
    def Parse(self):
        self.attributeList = self.attributeString.split(' ')
        inputAttributeCount = len(self.attributeList)

        if (inputAttributeCount != self.attributeCount):
            print(" Incorrect number of attributes in sphere input.")
        else:
            # correct number of attributes
            self.name = self.attributeList[0] 
            self.posX = self.attributeList[1]
            self.posY = self.attributeList[2]
            self.posZ = self.attributeList[3]
            self.scaleX = self.attributeList[4]
            self.scaleY = self.attributeList[5]
            self.scaleZ = self.attributeList[6]
            self.r = self.attributeList[7]
            self.g = self.attributeList[8]
            self.b = self.attributeList[9]
            self.ka = self.attributeList[10]
            self.kd = self.attributeList[11]
            self.ks = self.attributeList[12]
            self.kr = self.attributeList[13]
            self.n = self.attributeList[14]
        return 0

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.scaleX} {self.scaleY} {self.scaleZ} {self.r} {self.g} {self.b} {self.ka} {self.kd} {self.ks} {self.kr} {self.n}"

class Light:
    def __init__(self, attributeList):
        self.attributeList = attributeList
    
        # attributes for calculations
        self.name = ""
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.ir = 0
        self.ig = 0
        self.ib = 0

        self.attributeCount = 7
        
    def Parse(self):
        inputAttributeCount = len(self.attributeList)

        if (inputAttributeCount != self.attributeCount):
            print(" Incorrect number of attributes in light input.")
        else:
            # correct number of attributes
            self.name = self.attributeList[0] 
            self.posX = self.attributeList[1]
            self.posY = self.attributeList[2]
            self.posZ = self.attributeList[3]
            self.ir = self.attributeList[4]
            self.ig = self.attributeList[5]
            self.ib = self.attributeList[6]
        return 0

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.ir} {self.ig} {self.ib}"

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
        try:
            # correct number of attributes
            self.name = self.attributeList[1]
            self.posX = float(self.attributeList[2])
            self.posY = float(self.attributeList[3])
            self.posZ = float(self.attributeList[4])
            self.ir = float(self.attributeList[5])
            self.ig = float(self.attributeList[6])
            self.ib = float(self.attributeList[7])
            return 0 # success
        except Exception as e:
            print(f" An error occured: {e}")
            return -1 # failure

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.ir} {self.ig} {self.ib}"

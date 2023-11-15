class Sphere:
    def __init__(self, attributeList):
        self.attributeList = attributeList
    
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
        inputAttributeCount = len(self.attributeList)

        try:
            # TODO: do correct casting of numbers
            self.name = self.attributeList[1] 
            self.posX = self.attributeList[2]
            self.posY = self.attributeList[3]
            self.posZ = self.attributeList[4]
            self.scaleX = self.attributeList[5]
            self.scaleY = self.attributeList[6]
            self.scaleZ = self.attributeList[7]
            self.r = self.attributeList[8]
            self.g = self.attributeList[9]
            self.b = self.attributeList[10]
            self.ka = self.attributeList[11]
            self.kd = self.attributeList[12]
            self.ks = self.attributeList[13]
            self.kr = self.attributeList[14]
            self.n = self.attributeList[15]
        except Exception as e:
            print(f" An error occured: {e}")

        return 0

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.scaleX} {self.scaleY} {self.scaleZ} {self.r} {self.g} {self.b} {self.ka} {self.kd} {self.ks} {self.kr} {self.n}"

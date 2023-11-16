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
            self.posX = float(self.attributeList[2])
            self.posY = float(self.attributeList[3])
            self.posZ = float(self.attributeList[4])
            self.scaleX = float(self.attributeList[5])
            self.scaleY = float(self.attributeList[6])
            self.scaleZ = float(self.attributeList[7])
            self.r = float(self.attributeList[8])
            self.g = float(self.attributeList[9])
            self.b = float(self.attributeList[10])
            self.ka = float(self.attributeList[11])
            self.kd = float(self.attributeList[12])
            self.ks = float(self.attributeList[13])
            self.kr = float(self.attributeList[14])
            self.n = float(self.attributeList[15])
            return 0 # success
        except Exception as e:
            print(f" An error occured: {e}")
            return -1 # failure

    def PrintShort(self):
        return f"\nname: {self.name}\nx: {self.posX}\ny: {self.posY}\nz: {self.posZ}"

    def __str__(self):
        return f"\n{self.name} {self.posX} {self.posY} {self.posZ} {self.scaleX} {self.scaleY} {self.scaleZ} {self.r} {self.g} {self.b} {self.ka} {self.kd} {self.ks} {self.kr} {self.n}"

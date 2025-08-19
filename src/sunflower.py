import objectbase
import sunlight

class Sunflower(objectbase.ObjectBase):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        self.hasSunlight = False

    def preSummon(self):
        self.hasSunlight = True

    def hasSummon(self):
        return self.hasSunlight

    def doSummon(self):
        if self.hasSummon():
            self.hasSunlight = False
            return sunlight.SunLight(2,(self.pos[0]+20,self.pos[1]-10))


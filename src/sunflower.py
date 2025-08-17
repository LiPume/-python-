import objectbase
import sunlight

class Sunflower(objectbase.ObjectBase):
    def __init__(self,id,pos):
        super(Sunflower,self).__init__(id,pos)
        self.sunLights = []

    def preSummon(self):
        sl = sunlight.SunLight(2,(self.pos[0]+20,self.pos[1]-10))
        self.sunLights.append(sl)

    def update(self):
        super(Sunflower,self).update()
        for sl in self.sunLights:
            sl.update()

    def draw(self,ds):
        super(Sunflower,self).draw(ds)
        for sl in self.sunLights:
            sl.draw(ds )

import objectbase


class PeaBullet(objectbase.ObjectBase):


    def checkPosition(self):
        b = super(PeaBullet, self).checkPosition()
        if b:
            self.pos[0] += 4
        return b
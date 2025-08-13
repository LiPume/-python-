import image

class ObjectBase(image.Image):
    def __init__(self,pathFmt,pathIndex,pos,size=None,pathIndexCount=0):
        super(ObjectBase,self).__init__(pathFmt,pathIndex,pos,size,pathIndexCount)

    def upadte(self):
        self.checkImageIndex()
        self.checkPosition()

    def checkImageIndex(self):
        pass

    def checkPosition(self):
        pass
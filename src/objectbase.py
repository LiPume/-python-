import time

import image
from src import data_object


class ObjectBase(image.Image):
    def __init__(self,id,pos):
        self.id = id
        self.preIndexTime = 0
        self.prePositionTime = 0
        super(ObjectBase,self).__init__(
            self.getData()['PATH'],
            0,
            pos,
            self.getData()['SIZE'],
            self.getData()['IMAGE_INDEX_MAX']
        )

    def getData(self):
        return data_object.data[self.id]

    def getPositionCD(self):
        return self.getData()['POSITION_CD']

    def getImageIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']

    def update(self):
        self.checkImageIndex()
        self.checkPosition()

    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= 0.2:
            return
        self.preIndexTime = time.time()
        idx = self.pathIndex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)


    def checkPosition(self):
        if time.time() - self.prePositionTime <= self.getPositionCD():
            return False
        self.prePositionTime = time.time()
        return True
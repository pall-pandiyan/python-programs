import math

class volumeClass(object):
    def cylinderVolume(self,radious,height):
        return float(math.pi*radious*radious*height)
    def cubeVolume(self,length,width,height):
        return float(length*width*height)

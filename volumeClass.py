import math

class volumeClass:
    def cylinderVolume(self, radious, height):
        return float(math.pi*radious*radious*height)
    def cubeVolume(self, length, width, height):
        return float(length*width*height)

vc = volumeClass()
print("Cube Volume:",vc.cubeVolume(15, 3, 2))
print("Cylinder Volume:",vc.cylinderVolume(15, 3))
from math import *

class Sphere:

    def __init__(self, r):
        self.radius = r
        self.volume = 0
        self.area = 0
        

    def getRadius (self):
        return self.radius
        

    def surfaceArea(self):
        r= self.radius
        self.area = (4*pi*(r**2))
        return self.area
        

    def volume(self):
        r=self.radius
        self.volume = ((4/3)*pi*(r**3))
        return self.volume

def main():
    r=float(input("Enter a number for the radius: "))
    sphere= Sphere(r)

    volumeofsphere= ((4/3)*pi*(r**3))
    areaofsphere= (4*pi*(r**2))
    print("The volume of the sphere is: ", volumeofsphere)
    print("The area of the sphere is: ", areaofsphere)

if __name__ == '__main__':
    main()

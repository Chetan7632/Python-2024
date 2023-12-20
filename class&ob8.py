class Rectangle:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def area(self):
        a=self.l*self.b
        print("Area of Rect=",a)
    def volume(self):
        v=self.l*self.b*self.h
        print("Volume of Rect=",v)
ob=Rectangle(6,7.9,4.3)
ob.area()
ob.volume()
    

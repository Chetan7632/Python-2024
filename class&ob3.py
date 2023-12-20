class Area:
    def circle(self,r):
        self.r=r
        a=3.14*r*r
        print("Area of Circle=",a)
    def rect(self,l,b):
        self.l=l
        self.b=b
        a=l*b
        print("Area of Rectangle=",a)
    def triangle(self,b,h):
        self.b=b
        self.h=h
        a=0.5+(b*h)
        print("Area of Triangle=",a)
    def square(self,s):
        self.s=s
        a=s*s
        print("Area of Square=",a)
ob=Area()
ob.circle(5)
ob.rect(3,7)
ob.triangle(8,3.5)
ob.square(4)

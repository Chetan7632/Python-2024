class Volume:
    def cylinder(self,r,h):
        self.r=r
        self.h=h
        v=3.14*r*r*h
        print("Volume of Cylinder=",v)
    def circle(self,r,h):
        self.r=r
        self.h=h
        v=(1/3)*3.14*r*r*h
        print("Volume of Circle=",v)
    def sphere(self,r):
        self.r=r
        v=4/3*3.14*r*r
        print("Volume of Sphere=",v)
ob=Volume()
ob.cylinder(3,7)
ob.circle(4.3,9.6)
ob.sphere(7)

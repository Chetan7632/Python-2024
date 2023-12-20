class Student:
    def __init__(self,rno,name,per):
        self.rno=rno
        self.name=name
        self.per=per
    def disp(self):
        print("Roll No=",self.rno)
        print("Name=",self.name)
        print("Per=",self.per)
ob=Student(11,"om",77.66)
ob.disp()

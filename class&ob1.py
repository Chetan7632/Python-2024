class Student:
    def accept(self,rno,name,per):
        self.rno=rno
        self.name=name
        self.per=per
    def disp(self):
        print("Roll No=",self.rno)
        print("Name=",self.name)
        print("Percentage=",self.per)
ob=Student()
ob.accept(101,"om",55.66)
ob.disp()

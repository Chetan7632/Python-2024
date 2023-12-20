class Student:
    def accept(self):
        self.rno=input("Enter Roll no:")
        self.name=input("Enter Name:")
        self.per=input("Enter Percentage:")
    def disp(self):
        print("Roll No=",self.rno)
        print("Name=",self.name)
        print("Percentage=",self.per)
ob=Student()
ob.accept()
ob.disp()

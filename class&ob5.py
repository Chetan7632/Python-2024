class Student:
    def __init__(self):
        self.rno=input("Enter Roll No:")
        self.name=input("Enter Name:")
        self.per=input("Enter Per:")
    def disp(self):
        print("Roll No=",self.rno)
        print("Name=",self.name)
        print("Per=",self.per)
ob=Student()
ob.disp()

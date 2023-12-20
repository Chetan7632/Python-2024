class Demo:
    def __init__(self):
        self.s1=input("Enter String:")
    def print_string(self):
        print("String in UpperCase=",self.s1.upper())
        print("Reverse word by word=")
        self.s1=self.s1.lower()
        l1=self.s1.split(" ")
        for s in l1:
        print(s[::-1],end=" ")
ob=Demo()
ob.get_string()
ob.print_string()

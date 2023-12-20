class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
       return a/b

ob=Calculator()
print("Addtion=",ob.add(11,44))
print("Substraction=",ob.sub(11,443))
print("Multiplication=",ob.mul(11,44))
print("Division=",ob.div(11,44))

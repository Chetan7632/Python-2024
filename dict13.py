d1={"om":"66","vishal":"88","aman":"55","aba":"79"}
flag=True
while flag:
    name=input("Enter Name:")
    per=input("Enter Per:")
    if name in d1:
        print("Name Already Exists")
    else:
        flag=False
d1[name]=per
print(d1)

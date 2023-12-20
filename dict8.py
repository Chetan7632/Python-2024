d={"om":"55.77","dada":"77.88","aman":"66.77","sai":"46"}
name=input("Enter name of Student:")
if name in d.keys():
    print("Marks=",d[name])
else:
    print("Not Found")

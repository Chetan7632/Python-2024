d={"om":"55.77","dada":"77.88","aman":"66.77","sai":"46"}
name=input("Enter name of Student:")
for k in d:
    if k==name:
        print("Marks=",d[k])
        break
else:
    print("Not Found")

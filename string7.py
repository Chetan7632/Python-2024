a=[]
flag=True
while flag:
    print("1-insert \n 2-del \n 3-disp \n 4-exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        num=input("Enter Value:")
        a.append(num)
        print("Insert succ.....")
    elif ch==2:
        del a[0]
        print("Deleted...")
    elif ch==3:
        print(a)
    else:
        flag=False

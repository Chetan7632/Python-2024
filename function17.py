def show():
    f,s=0,1
    while True:
        t=f+s
        yield t
        f,s=s,t
n=int(input("Enter Limit:"))
ob=show()
print(0,1,end=" ")
for i in range(-1,n):
    print(next(ob),end=" ")

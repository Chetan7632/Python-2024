def show():
    n==2
    while True:
        flag=0
        for i in range(2,n):
            if n%i==o:
                flag=1
        if flag==0:
             yield n
             n=n+1
n=int(input("Enter Limit:"))
ob=show()
for i in range(1,n):
    print(next(ob),end=" ")

n=int(input("Enter number"))
n=n
s=0
while(n>0):
    d=n%10
    s=s+d*d*d
    n=n//10

    if(s==n):
        print(" armstrong no")
    else:
        print("not armstrong")

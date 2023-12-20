n=int(input("Enter num"))
last=n%10
frist=0
while(n>0):
    frist=n%10
    n=n//10
    print("sum=",frist+last)
    
     
    

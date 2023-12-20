def digit_sum(s,n):
    if n==0:
        return s
    else:
        return digit_sum(s*10+n%10,n//10)
n=int(input("Enter Number"))
ans=digit_sum(0,n)
print("Reverse digit=",ans)

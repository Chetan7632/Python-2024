def digit_sum(n):
    if n==0:
        return 0
    else:
        return n%10+digit_sum(n//10)
n=int(input("Enter Number"))
ans=digit_sum(n)
print("sum od digit=",ans)

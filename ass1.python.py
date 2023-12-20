n=input("Enter Number:")
n=int(n)
ec=0
oc=0
zc=0
while n>0:
  d=n%10
  n=n//10
 if d==0:
  zc=zc+1
 elif d%2==0:
  ec=ec+1
 elif d%2!=0:
  oc=oc+1
  print("Even No=",ec)
  print("Odd No=",oc)
  print("Zero No=",zc)

def show():
    a=2
    while True:
        yield a
        a=a+2
n=int(input("Enter How many even numbers do you want to print:"))
ob=show()
for i in range(0,n):
    print(next(ob))

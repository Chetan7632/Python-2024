def show():
    a=5
    yield a
    a=a+1
    yield a
    a=a+5
    yield a
x=show()
print("Value=",next(x))
print("Value=",next(x))
print("Value=",next(x))

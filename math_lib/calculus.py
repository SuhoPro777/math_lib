def it(func,a,b,n=1000):
    h=(b-a)/n
    s=0.5*func(a)+0.5*func(b)
    for i in range(1,n):
        s+=func(a+i*h)
    return s*h

def df(func,x,dx=1e-6):
    return (func(x+dx)-func(x))/dx
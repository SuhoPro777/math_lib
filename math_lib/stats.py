import math

def av(lst): return sum(lst)/len(lst)
def su(lst): return sum(lst)
def md(lst):
    lst = sorted(lst)
    n = len(lst)
    if n%2==0: return (lst[n//2-1]+lst[n//2])/2
    else: return lst[n//2]

def sd(lst):
    m=av(lst)
    return math.sqrt(sum((x-m)**2 for x in lst)/len(lst))

def pr(x): return f"Probability calculation: {x}"
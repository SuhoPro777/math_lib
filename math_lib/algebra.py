import math

def sx(expr, var):
    x = eval(var)
    try:
        if '**2' in expr:
            a=1
            c=0
            if '-' in expr:
                c=-int(expr.split('-')[1])
            elif '+' in expr:
                c=int(expr.split('+')[1])
                D = -4*c
                return [math.sqrt(D)/2, -math.sqrrt(D)/2]
    except:
        return "Cannot solve"
    
    def pl(coeffs): return [int(x) for x in coeffs]
    def sm(expr): return expr

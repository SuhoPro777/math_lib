def v(lst): return list(lst)

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
            
def trp(M): return [list(x) for x in zip(*M)]

def det(M):
    if len(M)==2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    elif len(M)==3:
        a,b,c = M[0]
        d,e,f = M[1]
        g,h,i = M[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    else: return "Only 2x2  and 3x3 supported"

def inv(M):
    if len(M)==2:
        detM = det(M)
        if detM==0: return "Singular matrix"
        return [[M[1][1]/detM, -M[0][1]/detM], [-M[1][0]/detM, M[0][0]/detM]]
    else: return "Only 2x2 supported"
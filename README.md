# math_lib

math_lib is a lightweight, easy-to-use Python math library.  
It provides basic mathematics, linear algebra, calculus, trigonometry, algebra, and statistics functions — all in one package, with no external dependencies.

## Features

### Basic Mathematics
- sq(x) – square root  
- ex(x) – exponential  
- lg(x, base=10) – logarithm  
- fct(n) – factorial  

### Trigonometry (trid.py)
- s(x) – sine  
- c(x) – cosine  
- t(x) – tangent  
- is_(x) – arcsin  
- ic(x) – arccos  
- it(x) – arctan  
- rad(x) – degrees to radians  
- deg(x) – radians to degrees  
- hyp(a, b) – hypotenuse  

### Linear Algebra (linear.py)
- v(lst) – create vector  
- mm(A,B) – matrix multiplication  
- trp(M) – transpose matrix  
- det(M) – determinant (2x2 or 3x3)  
- inv(M) – inverse (2x2)  

### Calculus (calculus.py)
- it(func, a, b, n=1000) – numerical integral  
- df(func, x) – numerical derivative  

### Algebra (algebra.py)
- sx(expr) – solve simple quadratic equation  
- pl(coeffs) – polynomial list  
- sm(expr) – simplify expression (placeholder)  

### Statistics (stats.py)
- av(lst) – mean  
- su(lst) – sum  
- md(lst) – median  
- sd(lst) – standard deviation  
- pr(x) – probability placeholder  

---

## Installation

You can install directly from GitHub:

`bash
pip install git+https://github.com/yourusername/math_lib.git
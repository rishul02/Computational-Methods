def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection(a,b,tolerance = 1e-5):
    if f(a)*f(b) >= 0:
        return None
    while (b - a)/2 > tolerance:
        c = (a + b)/2
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b =c 
        else:
            a = c
    return (a+b)/2

limit1 = 1
limit2 = 3

if f(limit1) * f(limit2) >= 0:
    print("The function does not change signs on the interval. Try different limits.")
else:
    root_bisection = bisection(limit1, limit2)
    if root_bisection is None:
        print("No root found in the given interval.")
    else:
        print("Bisection root:", root_bisection)
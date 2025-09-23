def f(x): return x**3 - 6*x**2 + 11*x - 6

def false_position(a, b, tolerance=1e-5, max_iter=100):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * f(b) > 0:
        return None   
    
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tolerance or abs(b - a) < tolerance:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c  
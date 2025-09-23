def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def secant(x0, x1, tolerance=1e-5, max_iter=100):
    if f(x0) == 0:
        return x0
    if f(x1) == 0:
        return x1

    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        denominator = f_x1 - f_x0
        if denominator == 0:
            return None
        
        x2 = x1 - f_x1 * (x1 - x0) / denominator
        
        if abs(x2 - x1) < tolerance or abs(f(x2)) < tolerance:
            return x2
        
        x0, x1 = x1, x2

    return x2

root_secant = secant(1, 2)
if root_secant is not None:
    print(f"Secant root: {root_secant:.6f}")
else:
    print("No root found with Secant method.")

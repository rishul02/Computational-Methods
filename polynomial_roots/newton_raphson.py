def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    return 3*x**2 - 12*x + 11

def newton_raphson(x0, tolerance=1e-5, max_iter=100):
    if f(x0) == 0:
        return x0

    x = x0
    for _ in range(max_iter):
        dfx = df(x)
        if dfx == 0:
            return None

        x_new = x - f(x) / dfx
        if abs(f(x_new)) < tolerance or abs(x_new - x) < tolerance:
            return x_new
        x = x_new

    return x

root_newton = newton_raphson(2)
if root_newton is not None:
    print(f"Newton-Raphson root: {root_newton:.6f}")
else:
    print("No root found with Newton-Raphson method.")

def g(x):
    return (6*x**2 - 11*x + 6)**(1/3)

def fixed_point(x0, tolerance=1e-5, max_iter=100):
    if abs(g(x0) - x0) < tolerance:
        return x0

    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new


    return None

root_fp = fixed_point(2)
if root_fp is not None:
    print(f"Successive Approximation root: {root_fp:.6f}")
else:
    print("No root found with Fixed Point method.")

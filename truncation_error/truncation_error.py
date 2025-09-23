import math

x = 1
true_value = math.e


n_terms = int(input("Enter the number of terms of the approximation: "))

approx = sum([(x**k)/math.factorial(k) for k in range(n_terms)])
error = true_value - approx

print(f"True value of e^1 : {true_value}")
print(f"For n = {n_terms}")
print(f"Approximation = {approx:.6f}")
print(f"Truncation Error = {error:.6e}")
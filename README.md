# Computational-Methods in Python
Overview
This repository demonstrates basic computational methods in Python:

Truncation Error Analysis – Using the exponential series ex for x=1.
Polynomial Root-Finding – Solving x3−6x2+11x−6=0 with multiple numerical methods.

It highlights both error analysis and numerical solution techniques in computational mathematics.

1. Truncation Error

        Objective:
                  Compute ex using a truncated Taylor series and analyze the truncation error.
   
        Method:
                ex=1+1!x+2!x2+3!x3+⋯
   
        Truncation Error:            
                En=ex−k=0∑nk!xk
                Observation:
                The truncation error decreases as more terms are included.

2. Solving Polynomial Equations

        Polynomial:
                   f(x)=x3−6x2+11x−6
   
        Methods Implemented:
                Bisection Method – Brackets a root and halves the interval until convergence.
             
                False Position (Regula Falsi) – Uses secant line for faster convergence than bisection.
                  
                Newton-Raphson Method – Open method using tangent lines (requires derivative).
                  
                Secant Method – Uses two points and secant lines; derivative not required.
              
                Successive Approximation (Fixed Point Iteration) – Iteratively applies x=g(x) until convergence.
               
        Observation:             
                Methods converge to the roots x=1,2,3.              
                Convergence speed and reliability vary by method.                
                Good initial guesses are essential for open methods like Newton-Raphson and Secant.

5. Requirements

                Python 3.x
                Libraries: math, numpy (optional)

6. References:
   
       Burden, R.L., & Faires, J.D. Numerical Analysis, 10th Edition.
       Chapra, S.C., & Canale, R.P. Numerical Methods for Engineers.

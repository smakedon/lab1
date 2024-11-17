import numpy as np
import matplotlib.pyplot as plt

# f(x)=exp(2x^3+3x^2-5)

def f(x):
    return np.exp(2*x**3+3*x**2-5)

def lagrange_polynomial(x_i, y_i, x):
    n = len(x_i)
    result = 0.0
    for i in range(n):
        l_i = 1.0
        for j in range(n):
            if i != j:
                l_i *= (x-x_i[j])/(x_i[i]-x_i[j])
        result += y_i[i]*l_i
    return result

def piece_interpolate (x_i, y_i, x):
    n = len(x_i)
    for i in range((n)-1):
        if x_i[i]<=x<=x_i[i+1]:
            return y_i[i]+(y_i[i+1]-y_i[i])/(x_i[i+1]-x_i[i])*(x-x_i[i])
        return 0

def plot (a, b, n):
    h = (b-a)/(n-1)
    x_i = [a+i*h for i in range(n)]
    y_i = f(np.array(x_i))
    x = np.linspace(a, b, 500)
    pl_true = f(x)

    pl_lagrange = [lagrange_polynomial(x_i, y_i, xj) for xj in x]
    lagrange_error = np.abs(pl_true-pl_lagrange)

    y_piecewise = [piece_interpolate(x_i, y_i, xj) for xj in x]
    piecewise_error = np.abs(pl_true- y_piecewise)


def anl_error(a, b, n_val):
    results = []
    for n in n_val:
        delta_lagrange, delta_piecewise = plot(a, b, n)
        results.append((n, delta_lagrange, delta_piecewise))
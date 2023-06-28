import numpy as np
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid

a, b = smp.symbols('a b', real=True, positive=True)
x = smp.symbols('x', real=True)
f = smp.cos(b*x)* smp.exp(-a*x)
r=smp.integrate(f, x).simplify()
print(r)
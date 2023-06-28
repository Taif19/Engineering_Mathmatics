#modify done from source =youtube_channel/Python Tutorial Series/integrals1.ipynb

import numpy as np
import sympy as smp
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid
from math import pi 

x= smp.symbols('x', real=True)
n= smp.symbols('n', real=True, positive=True)
f = (x+x*x)*smp.cos(n*x)
r=smp.integrate(f, (x, 0, 2*smp.pi)).simplify()
print(r)

# import scipy.integrate.dblquad
from scipy import integrate
  
f = lambda y, x: x * y**2
  
# using scipy.integrate.dblquad() method
I = integrate.dblquad(f, 0, 3, lambda x: 0, lambda x: 1)
  
print(I)
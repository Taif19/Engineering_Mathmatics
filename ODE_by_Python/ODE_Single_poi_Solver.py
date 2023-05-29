from scipy.integrate import solve_ivp

# function that returns dy/dt
def model(t,y):
   k = 0.3
   dydt = -k * y
   return dydt

# initial condition
y0 = [5]

# solve ODE
res = solve_ivp(model,[0,10],y0,dense_output=True)
y = lambda t: res.sol(t)[0]

for t in [2,3,3.4]:
    print(f'y({t}) = {y(t)}')

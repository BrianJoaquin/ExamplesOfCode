from pylab import plot,show
from numpy import pi

# Defining the differential equation
def accel(x):
    a = -x / m
    return a

# Potential energy corresponding to the acceleration above: ma = - dV/dx
def potential(x):
    V = x*x/2.0
    return V

# Entering initial values
x = 1.0
dt = pi / 50
m = 1.0
# Initial half step for v, it is now v at time dt/2
v = accel(0) * dt / 2

# Creating lists to plot future points
xpoints = []
ypoints = []


# Computationally solving the differential equation
for time in range(1,100):
    t = dt * time
    x += v * dt
# Update v (by *half* a time step) to same integer time step
# So x,v are known simultanously
    v_aux = v + dt / 2.0 * accel(x)
# Compute total energy
    e = m * v_aux ** 2/2 + potential(x)
# Update v from previous half-integer time step to next half-integer time step
    v += accel(x) * dt
    xpoints.append(t)
    ypoints.append(x)
    print(v, e)

plot(xpoints, ypoints)
show()

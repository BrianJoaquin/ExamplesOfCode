from pylab import plot,show
from numpy import pi

# Defining the differential equation
def accel(x, t):
    a = -x
    return a

# Entering initial values
v = 1
x = 1
dt = pi / 20

# Creating lists to plot future points
xpoints = []
ypoints = []

# Computationally solving the differential equation
for time in range(1,100):
    t = dt * time
    x += v * dt
    v += accel(x,t)
    xpoints.append(t)
    ypoints.append(x)
    print(v)

plot(xpoints, ypoints)
show()

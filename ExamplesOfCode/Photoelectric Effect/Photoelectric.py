from numpy import loadtxt
from pylab import plot, show

# Loading in the data
m = loadtxt("insert directory to millikan.txt here", float)

# Slicing the two columns into X and Y points
xpoints = m[:,0]
ypoints = m[:,1]

# Calculating the Slope and the Y-intercept using the Least Squares formula
XXVal = xpoints * xpoints
XYVal = xpoints * ypoints

AX = sum(xpoints) / len(xpoints)
AY = sum(ypoints) / len(ypoints)

XXVal = xpoints * xpoints
XYVal = xpoints * ypoints

SSXX = sum(XXVal) - len(XXVal) * AX * AX
SSXY = sum(XYVal) - len(XYVal) * AX * AY

Slope = SSXY / SSXX
Intercept = AY - Slope * AX

# Plotting the corresponding X and Y points, as well as plotting the regression line
linex = []
liney = []
linex.append(xpoints[0])
linex.append(xpoints[len(xpoints) - 1])
liney.append(Intercept + Slope * xpoints[0])
liney.append(Intercept + Slope * xpoints[len(xpoints) - 1])
plot(linex, liney)
plot(xpoints, ypoints, 'bo')
print(Slope, Intercept)
show()

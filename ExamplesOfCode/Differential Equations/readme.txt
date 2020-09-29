The Physics Behind the Code:

Physics is generally the study of how objects move/interact with each other. 
However, there are times that we don't know the path an object is moving in, but rather just it's speed (AKA velocity), or it's acceleration.
This isn’t the end of the world, as we can use these variables to create differential equations, which are equations that are derived from the objects movement, and work backwards.
But there is a catch, solving differential equations analytically (by a human) is very challenging, and often not possible.
Thus the need for computer computation and approximation arises.

Euler Method Code:

The Euler method of numerical approximation is a method that brute force calculates the solution of the differential equation.
For example, it takes the differential equation ∆𝑥/∆𝑡=−𝑥 for example, transforms it into ∆𝑥=−𝑥∗∆𝑡, and repeatedly runs calculations through this equation with small values of ∆𝑡 in order to approximate the values of the function. 
We can then graph these values in order to determine the solution of the differential equation. This method can also be used to determine second order differential equations as well.
In my programs I define a function which represents a differential equation which and is also able to be solved analytically (it is an exponential function) in order to confirm the approximation works.

Verlet Method Code:

The Verlet method of numerically approximating the solutions to differential equations calculates these solutions by using a “Leap frog” method of integration. 
Unlike the Euler method of numerical approximation that calculates the position and velocity of the object at the same time intervals, the Leap frog method begins by calculating the velocity of the object in a half step time interval.
This provides a more precise calculation.
In order to confirm that my program works I use a differential equation that can be solved analytically, which turns out to be a cosine function. 

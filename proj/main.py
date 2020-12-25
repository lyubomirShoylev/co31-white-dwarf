# initialize the white dwarf as an ode
# import constants
# use the functional form of the three different limits
# integrate and get solutions
# plots for the lab book/report

# TODO documentation, the if __name__ == __main__ and so on

# importing package like this since conda install does not play nicely
import ode
import numpy as np
import math
import matplotlib.pyplot as plt

x = 0.0
y = np.array([0, 1])

def SHO(x: float, y: np.ndarray):
    """
    docstring
    """
    return np.array([-1.0*y[1], y[0]])

def someODE(x: float, y: float):
    """
    docstring
    """
    return y*(2/(np.exp(x)+1)-1)

def someODEsln(x: float):
    """
    docstring
    analytical solution to the ODE in someODE
    """
    return 12*np.exp(x)*((np.exp(x)+1)**(-2))

h = 0.001

lel = np.linspace(0,10,10001)
func = someODE
eul = ode.ODEinit(x, y, func, h, lel)
eul.integrate(1)

heu = ode.ODEinit(x, y, func, h, lel)
heu.integrate(2)

rk4 = ode.ODEinit(x, y, func, h, lel)
rk4.integrate(3)

# TODO collect the plotting procedure nicely

# analytical = np.cos(lel)
analytical = someODEsln(lel)
plt.plot(lel, analytical - eul.yOut[:,1])
plt.plot(lel, analytical - heu.yOut[:,1])
plt.plot(lel, analytical - rk4.yOut[:,1])

plt.show()
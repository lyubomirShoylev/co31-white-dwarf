# initialize the white dwarf as an ode
# import constants
# use the functional form of the three different limits
# integrate and get solutions
# plots for the lab book/report

# TODO documentation, the if __name__ == __main__ and so on

# importing package like this since conda install does not play nicely
from numpy.core.function_base import linspace
from lib import ode,whiteDwarf, derivatives
import numpy as np
import math 
import matplotlib.pyplot as plt
import scipy.constants as const
import warnings
warnings.filterwarnings("error")

# np.fft.fft()

x = 0.0
y = np.array([0, 1])
# h = 0.001

# lel = np.linspace(0,10,10001)
# func = derivatives.someODE
# eul = ode.ODEinit(x, y, func, h, lel)
# eul.integrate(1)

# heu = ode.ODEinit(x, y, func, h, lel)
# heu.integrate(2)

# rk4 = ode.ODEinit(x, y, func, h, lel)
# rk4.integrate(3)

yo = linspace(1,1e7,num=10000001)
rho = linspace(1e6, 1e14, 40)
rAndM = np.zeros((40,2))
for i in range(40):
    star = whiteDwarf.WhiteDwarf(rho[i], yo, 1)
    star.integrate(3)

    rAndM[i,:] = star.getRadiusMass()

np.savetxt('values.csv', rAndM, delimiter=',')


rho1 = 1.0e9
rho2 = 1.0e13
star1 = whiteDwarf.WhiteDwarf(rho1, yo, 1)
star1.integrate(3)

radius1, mass1 = star1.getRadiusMass()
print(radius1/1000, mass1/1.988e30)

star2 = whiteDwarf.WhiteDwarf(rho2, yo, 1)
star2.integrate(3)

# TODO collect the plotting procedure nicely

# analytical = np.cos(lel)
# analytical = derivatives.someODEsln(lel)
# plt.plot(lel, analytical - eul.yOut[:,1])
# plt.plot(lel, analytical - heu.yOut[:,1])
# plt.plot(lel, analytical - rk4.yOut[:,1])
plt.plot(yo, star1.yOut[:,0])
plt.plot(yo, star2.yOut[:,0])
plt.show()
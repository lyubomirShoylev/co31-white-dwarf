# initialize the white dwarf as an ode
# import constants
# use the functional form of the three different limits
# integrate and get solutions
# plots for the lab book/report

# TODO documentation and so on

from numpy.core.function_base import linspace
# from .modules import ode,whiteDwarf, derivatives
import modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

from multiprocessing import Pool, cpu_count
# h = 0.001

# lel = np.linspace(0,10,10001)
# func = derivatives.someODE
# eul = ode.ODEinit(x, y, func, h, lel)
# eul.integrate(1)

# heu = ode.ODEinit(x, y, func, h, lel)
# heu.integrate(2)

# rk4 = ode.ODEinit(x, y, func, h, lel)
# rk4.integrate(3)

yo = linspace(1,8.1e7,num=81000000)
# rho = linspace(1e6, 1e14, 40)
# rAndM = np.zeros((40,2))
# for i in range(40):
#     star = whiteDwarf.WhiteDwarf(rho[i], yo, 1)
#     star.integrate(3)

#     rAndM[i,:] = star.getRadiusMass()

# np.savetxt('values.csv', rAndM, delimiter=',')


# rho1 = 5.0e9
# rho2 = 1.0e13
# star1 = whiteDwarf.WhiteDwarf(rho1, yo, 2)
# star1.integrate(3)

# radius1, mass1 = star1.getRadiusMass()
# print(radius1/1000, mass1/1.988e30)

# star2 = whiteDwarf.WhiteDwarf(rho2, yo, 1)
# star2.integrate(3)

# TODO collect the plotting procedure nicely

# analytical = np.cos(lel)
# analytical = derivatives.someODEsln(lel)
# plt.plot(lel, analytical - eul.yOut[:,1])
# plt.plot(lel, analytical - heu.yOut[:,1])
# plt.plot(lel, analytical - rk4.yOut[:,1])
# plt.plot(yo, star1.yOut[:,1])
# plt.plot(yo, star2.yOut[:,0])
# plt.show()

# plt.plot(yo, star1.yOut[:,0])
# plt.plot(yo, star2.yOut[:,0])
# plt.show()

# kek = 1

l_results = []
np.savetxt
def lelODE(rho):
    star = modules.whiteDwarf(rho, yo, 1)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    print("Calculation done for rho = {}".format(rho))
    return [rho, radius/1000, mass/1.988e30]


def main():
    rhoVal = np.array([float(a)*10**b for b in range(6,15) for a in range(1,10)])
    with Pool(cpu_count(), maxtasksperchild=1) as executor:
        retour = executor.map(lelODE, rhoVal)
    
    np.savetxt("results.csv", np.array(retour), delimiter=',')


if __name__ == "__main__":
    main()
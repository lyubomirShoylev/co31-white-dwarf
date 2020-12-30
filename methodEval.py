# Test the error with the integrators and plot residuals
# NOTE we need some amount of iterations comparable to the white dwarf to 
# compate the methods


# lel = np.linspace(0,10,10001)
# func = derivatives.someODE
# eul = ode.ODEinit(x, y, func, h, lel)
# eul.integrate(1)

# heu = ode.ODEinit(x, y, func, h, lel)
# heu.integrate(2)

# rk4 = ode.ODEinit(x, y, func, h, lel)
# rk4.integrate(3)

# analytical = np.cos(lel)
# analytical = derivatives.someODEsln(lel)
# plt.plot(lel, analytical - eul.yOut[:,1])
# plt.plot(lel, analytical - heu.yOut[:,1])
# plt.plot(lel, analytical - rk4.yOut[:,1])
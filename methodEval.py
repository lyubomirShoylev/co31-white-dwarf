# Test the error with the integrators and plot residuals
# NOTE we need some amount of iterations comparable to the white dwarf to 
# compate the methods i.e. 1e6
from math import cos, sin

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.core.function_base import linspace

import modules
from modules.derivatives import SHO


def plots():
    # load data
    eul1= pd.read_csv("method1.csv")
    heun= pd.read_csv("method2.csv")
    rk4= pd.read_csv("method3.csv")
    eul2= pd.read_csv("method4.csv")
    
    # theoretical data
    x0 = 1.0
    step = 0.001
    span = np.array(step*linspace(1,1000000,num=1000000))
    # for eul1, heun, rk4
    theory = np.concatenate(([1], x0*np.cos(2*np.pi*span)))

    # 2*energy in systems/m
    c = 4*np.pi*np.pi
    enEul1 = eul1["xdot"]**2 + c*eul1["x"]**2
    enEul2 = eul2["xdot"]**2 + c*eul2["x"]**2
    enHeun = heun["xdot"]**2 + c*heun["x"]**2
    enRK4 = rk4["xdot"]**2 + c*rk4["x"]**2
    
    ##  plot 1 - oscill of eul1, eul2, heun
    plt.figure(1)
    plt.plot(eul1.index/1000, eul1["x"])
    plt.plot(eul2.index/1000, eul2["x"])
    plt.plot(heun.index/1000, heun["x"])
    #axis setup
    plt.xlim(0, 20)
    plt.xlabel("time t, s")
    plt.ylim(-2,2)
    plt.ylabel("position x(t)")
    plt.legend(["euler1", "euler2", "heun"])
    plt.show
    plt.savefig("eul12+heun.pdf")

    ## plot2 - (oscill - theory) of eul1, eul2, heun
    plt.figure(2)
    plt.plot(eul1.index/1000, eul1["x"] - theory)
    plt.plot(eul2.index/1000, eul2["x"] - theory)
    plt.plot(heun.index/1000, heun["x"] - theory)
    #axis setup
    plt.xlim(0, 20)
    plt.xlabel("time t, s")
    plt.ylim(-0.5,0.5)
    plt.ylabel("position x(t)")
    plt.legend(["euler1", "euler2", "heun"], loc="upper left")
    plt.show
    plt.savefig("eul12+heun-theory.pdf")

    ## plot3 - energy of eul1, eul2, heun
    plt.figure(3)
    plt.plot(enEul1.index/1000, abs(enEul1-c)/c)
    plt.plot(enEul2.index/1000, abs(enEul2-c)/c)
    plt.plot(enHeun.index/1000, abs(enHeun-c)/c)
    #axis setup
    plt.xlim(0, 200)
    plt.xlabel("time t, s")
    plt.ylim(1e-7,100000)
    plt.yscale('log')
    plt.ylabel("energy $\Delta E/E_0$")
    plt.legend(["euler1", "euler2", "heun"], loc="upper left")
    plt.show
    plt.savefig("eul12+heun+energy.pdf")

    ## plot4 - energy of heun, rk4
    plt.figure(4)
    plt.plot(enHeun.index/1000, abs(enHeun-c)/c, color='green')
    plt.plot(enRK4.index/1000, abs(enRK4-c)/c, color='red')
    #axis setup
    plt.xlabel("time t, s")
    plt.ylim(5e-7,1e-3)
    plt.yscale('log')
    plt.ylabel("energy $\Delta E/E_0$")
    plt.legend(["heun", "rk4"], loc="upper left")
    plt.show
    plt.savefig("heunRK4+energy.pdf")


def main():
    # initial parameters of the SHO
    x0 = 1.0
    step = 0.001
    y0 = x0*np.array([-sin(step), cos(step)])
    span = step*linspace(1,1000000,num=1000000)
    
    # do integration for the three methods
    for integ in [1,2,3]:
        ode = modules.ODEinit(y0, SHO, span)
        ode.integrate(integ)
        res = np.vstack((np.array([0,1]), ode.yOut))
        dfOut = pd.DataFrame(res, columns=["xdot", "x"])
        dfOut.to_csv("method{}.csv".format(integ), index=None)
    
    # additional integration for the euler method with a step 1/10th of original
    span2 = 0.1*step*linspace(1,10000000,num=10000000)
    ode = modules.ODEinit(y0, SHO, span2)
    ode.integrate(1)
    res = np.vstack((np.array([0,1]), ode.yOut))
    # keep the data only at the same moments as the other ones
    dfOut = pd.DataFrame(res[::10], columns=["xdot", "x"])
    dfOut.to_csv("method4.csv", index=None)

    plots()


if __name__=='__main__':
    main()    
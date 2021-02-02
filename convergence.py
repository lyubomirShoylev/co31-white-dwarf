"""convergence.py
This is an auxiliary script, which helps determine the convergence of 
computing white dwarf parameters and in turn judge the needed coarsness of 
the integration space. Many of the functions here are direct copies of the ones
in main.py; look there for more explanation. Outputs .csv files of calculations.
"""

import math
from datetime import datetime

# for saving files to csv (easier than the numpy implementation)
import pandas as pd
# for setup of integration grid
from numpy.core.function_base import linspace

# our library
import modules

# Direct copy of the method in main.py, only added a variable for the number of
# intervals in the space (since we are probing it). Additionally, computation
# time is also recorded (although it should be proportional to # of steps, so 
# techincally do no really need it)
def starInitNonRelativ(rhoC, n):
    startTime = datetime.now()
    span = linspace(1,4.0e7,num=n)
    star = modules.whiteDwarf(rhoC, span, 1)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    # for logging purposes
    print("Calculation done for rho = {}; elapsed time = {}".format(rhoC, datetime.now() - startTime))
    # return the three values rho in kg*m^(-3), radius in km/1000, mass in solar mass
    return [rhoC, radius/1000, mass/1.988e30]

# Direct copy of the method in main.py, only added a variable for the number of
# intervals in the space (since we are probing it). Additionally, computation
# time is also logged (although it should be proportional to # of steps, so 
# techincally do no really need it)
def starInitRelativ(rhoC, n):
    startTime = datetime.now()
    span = linspace(1,8.1e7,num=n)
    star = modules.whiteDwarf(rhoC, span, 2)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    # for logging purposes
    print("Calculation done for rho = {}; elapsed time = {}".format(rhoC, datetime.now() - startTime))
    # return the three values rho in kg*m^(-3), radius in km/1000, mass in solar mass
    return [rhoC, radius/1000, mass/1.988e30]

# Loop the three densities - two at the ends of the interval and one at the middle
for density in [1e6, 1e10, 1e14]:
    # Array to store all the answers of integration
    resNonRelativ = []
    # Loop over the different # of intervals/steps
    for i in [float(a)*10**b for b in range(2,8) for a in [1,2,4,8]]:
        rho, radius, mass = starInitNonRelativ(1e6, int(i))
        print("{} iterations: radius {}, mass {}".format(i, radius, mass))
        resNonRelativ.append([rho, radius, mass])

    # Record results to csv file
    dfNonRelativ = pd.DataFrame(resNonRelativ, columns=["rhoC", "radiusKM", "massSolMass", "time"])
    dfNonRelativ.to_csv(
        "convergenceE{}nonRelativ.csv".format(int(math.log10(density))),
        index=None
    )

    # Array to store all the answers of integration
    resRelativ = []
    # Loop over the different # of intervals/steps
    for i in [float(a)*10**b for b in range(2,8) for a in [1,2,4,8]]:
        rho, radius, mass = starInitRelativ(1e6, int(i))
        print("{} iterations: radius {}, mass {}".format(i, radius, mass))
        resRelativ.append([rho, radius, mass])

    # Record results to csv file
    dfRelativ = pd.DataFrame(resRelativ, columns=["rhoC", "radiusKM", "massSolMass", "time"])
    dfRelativ.to_csv(
        "convergenceE{}Relativ.csv".format(int(math.log10(density))),
        index=None
    )

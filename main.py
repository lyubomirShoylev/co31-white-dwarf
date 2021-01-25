# TODO documentation and so on

# parallel computing library
from multiprocessing import Pool, cpu_count

# numpy imports
import numpy as np
from numpy.core.function_base import linspace
a = np.bool8
# our white dwarf integrator module
import modules
# import time
from datetime import datetime
# TODO implement pandas to save all yOut values so we can plot some rho(r)
# for different values of rhoC
import pandas as pd
# initializes an instance of a white dwarf

# non-relativistic case
def starInitNonRelativ(rhoC):
    startTime = datetime.now()
    span = linspace(1,8.1e7,num=81000000)
    star = modules.whiteDwarf(rhoC, span, 1)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    print("Calculation done for rho = {}; elapsed time = {}".format(rhoC, datetime.now() - startTime))
    # return the three values rho in kg*m^(-3), radius in km/1000, mass in solar mass
    return [rhoC, radius/1000, mass/1.988e30]

# relativistic case
def starInitRelativ(rhoC):
    startTime = datetime.now()
    span = linspace(1,8.1e7,num=81000000)
    star = modules.whiteDwarf(rhoC, span, 2)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    print("Calculation done for rho = {}; elapsed time = {}".format(rhoC, datetime.now() - startTime))
    # return the three values rho in kg*m^(-3), radius in km/1000, mass in solar mass
    return [rhoC, radius/1000, mass/1.988e30]


def main():
    # the rho values to test in the range, change the list accordingly
    rhoVal = np.array([float(a)*10**b for b in range(6,15) for a in range(1,10)])

    # implement parallel computation of the ODEs

    # non-relativistic gas
    with Pool(cpu_count(), maxtasksperchild=1) as executor:
        # results are returned in a list in the order they were passed to the 
        # processes (FIFO).
        resNonRelativ = executor.map(starInitNonRelativ, rhoVal)

    # non-relativistic case
    np.savetxt("resultsNonRelativ.csv", np.array(resNonRelativ), delimiter=',')
    dfNonRel = pd.DataFrame(resNonRelativ, columns=["rhoC", "radiusKM", "massSolMass"])
    dfNonRel.to_csv(
        "nonRelativ210121.csv", index=None
    )

    # relativistic gas
    with Pool(cpu_count()-6, maxtasksperchild=1) as executor:
        # results are returned in a list in the order they were passed to the 
        # processes (FIFO).
        resRelativ = executor.map(starInitRelativ, rhoVal)
    
    # save the list in a .csv file



    # relativistic case
    np.savetxt("resultsRelativ.csv", np.array(resRelativ), delimiter=',')
    dfRel = pd.DataFrame(resRelativ, columns=["rhoC", "radiusKM", "massSolMass"])
    dfRel.to_csv("relativ210121.csv", index=None)


if __name__ == "__main__":
    main()

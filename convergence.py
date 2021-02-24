"""convergence.py
This is an auxiliary script, which helps determine the convergence of 
computing white dwarf parameters and in turn judge the needed coarseness of 
the integration space. Many of the functions here are direct copies of the ones
in main.py; look there for more explanation. Outputs .csv files of calculations.
"""
import math
from multiprocessing import Pool, cpu_count

# for saving files to csv (easier than the numpy implementation)
import pandas as pd
# solar mass for output scale
from astropy.constants import M_sun
# for setup of integration grid
from numpy.core.function_base import linspace

# our library
import modules


# Direct copy of the method in main.py, only added a variable for the number of
# intervals in the space (since we are probing it).
def starInitNonRelativ(myTuple):
    rhoC, n = myTuple
    span = linspace(1,8.1e7,num=n)
    star = modules.whiteDwarf(rhoC, span, 1)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    # return the three values No of iter, radius in km/1000, mass in solar mass
    return [n, radius/1000, mass/M_sun.value]

# Direct copy of the method in main.py, only added a variable for the number of
# intervals in the space (since we are probing it).
def starInitRelativ(myTuple):
    rhoC, n = myTuple
    span = linspace(1,8.1e7,num=n)
    star = modules.whiteDwarf(rhoC, span, 2)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    # return the three values No of iter, radius in km/1000, mass in solar mass
    return [n, radius/1000, mass/M_sun.value]

numberOfIterations = [int(float(a)*10**b) for b in range(2,8) for a in [1,2,4,8]]

# wrapped all actions in a main function because of the multiprocessing
def main():
    # Loop the three densities - two at the ends of the interval and one at the middle
    # multiprocessing copied from main.py
    for density in [1e6, 1e10, 1e14]:
        # quick hack to prepare an iterable for the multiprocessing pool
        # function, since our function needs two parameters
        poolIterable = [(density, n) for n in numberOfIterations]
        with Pool(cpu_count(), maxtasksperchild=1) as executor:
            # The executor.map(f, s) applies the function f to each member of the
            # iterable s and collects the results in a list following a First In 
            # First Out procedure, so the results collected are ordered by the
            # order in which they were in s, i.e. by central density values.
            resNonRelativ = executor.map(starInitNonRelativ, poolIterable)

        # Save results for non-relativistic case
        dfNonRel = pd.DataFrame(resNonRelativ, columns=["NoIter", "radiusKM", "massSolMass"])
        dfNonRel.to_csv(
            "convergenceE{}nonRelativ.csv".format(int(math.log10(density))),
            index=None
        )
        
        with Pool(cpu_count()-6, maxtasksperchild=1) as executor:
            # The executor.map(f, s) applies the function f to each member of the
            # iterable s and collects the results in a list following a First In 
            # First Out procedure, so the results collected are ordered by the
            # order in which they were in s, i.e. by central density values.
            resRelativ = executor.map(starInitRelativ, poolIterable)

        # Record results to csv file
        dfRelativ = pd.DataFrame(resRelativ, columns=["NoIter", "radiusKM", "massSolMass"])
        dfRelativ.to_csv(
            "convergenceE{}Relativ.csv".format(int(math.log10(density))),
            index=None
        )


if __name__ == '__main__':
    main()

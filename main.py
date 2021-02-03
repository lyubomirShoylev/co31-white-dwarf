"""main.py
The main script in this experiment. It calculates the values of the white dwarf
radius and mass for different central densities (initial conditions to solve
the ODE) by using our purpose built library and outputs them to a .csv file.
"""

# parallel computing library
from multiprocessing import Pool, cpu_count

# TODO look at usage below
import numpy as np
# for setup of integration grid
from numpy.core.function_base import linspace

# for saving files to csv (easier than the numpy implementation)
import pandas as pd

# our white dwarf integrator module
import modules

# Initialize a white dwarf with non-relativistic equation of state
def starInitNonRelativ(rhoC):
    """This function initializes a white dwarf with a non-relativistic equation
    of state and calculates its radius and mass, then returns the values.

    Parameters
    ----------
    rhoC : float
        The density of the center in kg*m^(-3), used to set the initial
        conditions for integration.

    Returns
    -------
    list
        Returns a three element list of the density in in kg*m^(-3), the radius
        in km/1000, and the mass in solar mass in this order.
    """
    # Integration grid, optimal step size determined on convergence ground
    # for more info look at convergence.py
    span = linspace(1,8.1e7,num=81000000)
    # Initialize the white dwarf and integrate
    star = modules.whiteDwarf(rhoC, span, 1)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    # return the three values rho in kg*m^(-3), radius in km/1000, mass in solar mass
    return [rhoC, radius/1000, mass/1.988e30]

# Initialize a white dwarf with relativistic equation of state
def starInitRelativ(rhoC):
    """This function initializes a white dwarf with a relativistic equation of 
    state and calculates its radius and mass, then returns the values.

    Parameters
    ----------
    rhoC : float
        The density of the center in kg*m^(-3), used to set the initial
        conditions for integration.

    Returns
    -------
    list
        Returns a three element list of the density in in kg*m^(-3), the radius
        in km/1000, and the mass in solar mass in this order.
    """
    # Integration grid, optimal step size determined on convergence ground
    # for more info look at convergence.py
    span = linspace(1,8.1e7,num=81000000)
    # Initialize the white dwarf and integrate
    star = modules.whiteDwarf(rhoC, span, 2)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    # return the three values rho in kg*m^(-3), radius in km/1000, mass in solar mass
    return [rhoC, radius/1000, mass/1.988e30]


def main():
    # TODO do we need this or just use the list as iterable?
    # the rho values to test in the range, change the list accordingly
    rhoVal = np.array([float(a)*10**b for b in range(6,15) for a in range(1,10)])

    # Implements parallel computation of the ODEs using multiple processes.
    # Computation is done over the range of central density values rhoVal.

    # Computation for non-relativistic gas. This process sets up the
    # multiprocessing and cleans up after the calculations are over.
    with Pool(cpu_count(), maxtasksperchild=1) as executor:
        # The executor.map(f, s) applies the function f to each member of the
        # iterable s and collects the results in a list following a First In 
        # First Out procedure, so the results collected are ordered by the
        # order in which they were in s, i.e. by central density values.
        resNonRelativ = executor.map(starInitNonRelativ, rhoVal)

    # Save results for non-relativistic case
    dfNonRel = pd.DataFrame(resNonRelativ, columns=["rhoC", "radiusKM", "massSolMass"])
    dfNonRel.to_csv("nonRelativRes.csv", index=None)

    # Computation for non-relativistic gas. This process sets up the
    # multiprocessing and cleans up after the calculations are over.
    with Pool(cpu_count()-6, maxtasksperchild=1) as executor:
        # The executor.map(f, s) applies the function f to each member of the
        # iterable s and collects the results in a list following a First In 
        # First Out procedure, so the results collected are ordered by the
        # order in which they were in s, i.e. by central density values.
        resRelativ = executor.map(starInitRelativ, rhoVal)
    
    # Save results for relativistic case
    dfRel = pd.DataFrame(resRelativ, columns=["rhoC", "radiusKM", "massSolMass"])
    dfRel.to_csv("relativRes.csv", index=None)


if __name__ == "__main__":
    main()

# TODO documentation and so on

# parallel computing library
from multiprocessing import Pool, cpu_count

# numpy imports
import numpy as np
from numpy.core.function_base import linspace

# our white dwarf integrator module
import modules as modules

# TODO implement pandas to save all yOut values so we can plot some rho(r)
# for different values of rhoC

# initializes an instance of a white dwarf
def starInit(rhoC):
    span = linspace(1,8.1e7,num=81000000)
    star = modules.whiteDwarf(rhoC, span, 2)
    star.integrate(3)

    radius, mass = star.getRadiusMass()
    print("Calculation done for rho = {}".format(rhoC))
    return [rhoC, radius/1000, mass/1.988e30]


def main():
    # the rho values to test in the range, change the list accordingly
    rhoVal = np.array([float(a)*10**b for b in range(6,15) for a in range(1,10)])

    # implement parallel computation of the ODEs
    with Pool(cpu_count(), maxtasksperchild=1) as executor:
        # results are returned in a list in the order they were passed to the 
        # processes (FIFO).
        res = executor.map(starInit, rhoVal)
    
    # save the list in a .csv file
    np.savetxt("resultsRelativ.csv", np.array(res), delimiter=',')


if __name__ == "__main__":
    main()

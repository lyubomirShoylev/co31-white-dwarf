import numpy as np
# for saving files to csv (easier than the numpy implementation)
import pandas as pd
# solar mass for output scale
from astropy.constants import M_sun
# for setup of integration grid
from numpy.core.function_base import linspace

# our white dwarf integrator module
import modules

# Integration grid, optimal step size determined on convergence ground
# for more info look at convergence.py
span = linspace(1,8.1e7,num=2000000)
# Initialize the white dwarf and integrate
star = modules.whiteDwarf(1e10, span, 2)
star.integrate(3)

radius, mass = star.getRadiusMass()
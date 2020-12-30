"""
Module containing facilities for numerically integrating general ODEs and white
dwarfs using either non-relativistic or relativistic equation of state.
"""

from .ode  import ODEinit
from .whiteDwarf import whiteDwarf

# TODO ask is it possible to import a module for all files in the directory,
# eg improt numpy for all
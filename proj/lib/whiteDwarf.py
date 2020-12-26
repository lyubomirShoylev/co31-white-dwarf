"""
White dwarf class
"""
from . import ode, derivatives
import numpy as np
import math
class whiteDwarf(ode.ODEinit):
    """
    docstring
    """
    def __init__(self, rhoC, range, regime):
        """
        docstring - override the ode init
        """
        # pre-filter the init_conditions of a white dwarf to fit a general ODE
        # the direction of init_condit determined by the eqn
        init_condit = np.array([rhoC, 4.0*math.pi*(range[0]**3)/3])
        # placeholder; determine it according to regime
        func = lambda x: x
        super(whiteDwarf, self).__init__(init_condit, func, range)
    
    # integrate part of odeinit

    def getRadiusMass(self):
        """
        docstring
        """
        # implement some cut-off, maybe regime-dependent, i.e. for non-relativ
        # we have some rho<<rhoC, for relativistic where rho changes sign
        (R,M) = self.yOut[-1,:]
        return (R, M)
    
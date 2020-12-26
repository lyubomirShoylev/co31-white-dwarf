"""
White dwarf class
"""
from . import ode, derivatives
import numpy as np
from scipy import constants as cs

class WhiteDwarf(ode.ODEinit):
    """
    docstring
    """
    def __init__(self, rhoC, span, regime=1):
        """
        docstring - override the ode init
        """
        # pre-filter the init_conditions of a white dwarf to fit a general ODE
        # the direction of init_condit determined by the eqn - current is rho,m
        # rhoC will be the scaling constant for the (rho, m)  vector in the 
        # chosen base.
        self.rhoC = rhoC
        init_condit = np.array([1.0, 1.0*(span[0]**3)])
        # determine func according to regime
        # TODO replace with dict for neatness (can do since execute only once)
        # scaling constant in the equation, choose l^3 * 4*pi/3 = 1
        self.scalar = -96*(54**(-1.0/3))*(cs.pi**(5.0/3))*cs.gravitational_constant*\
            cs.electron_mass*(cs.proton_mass**(5.0/3))*(rhoC**(1.0/3))*(cs.h**(-2.0))
        if regime == 1:
            func = lambda a, b: derivatives.nonRelativGas(a, b, self.scalar)
        elif regime == 2:
            func = lambda a, b: derivatives.relativGas(a, b, self.scalar)
        elif regime == 3:
            func = lambda a, b: derivatives.ultraRel(a, b, self.scalar)
        else:
            # implement throwing error (at the end)
            pass
        super(WhiteDwarf, self).__init__(init_condit, func, span)
    
    # integrate part of odeinit
    def integrate(self, integrator: int) -> None:
        """
        docstring
        """
        #fix init conditions
        super(WhiteDwarf, self).integrate(integrator)

    def getRadiusMass(self):
        """
        docstring
        """
        # implement some cut-off, maybe regime-dependent, i.e. for non-relativ
        # we have some rho<<rhoC, for relativistic where rho changes sign
        (R,M) = self.yOut[-1,:]
        return (R, M)
    
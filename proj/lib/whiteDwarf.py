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
        self.scalar = -(2**(13.0/3))*cs.pi*cs.gravitational_constant*\
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
        self.flagIntegr = False
        super(WhiteDwarf, self).__init__(init_condit, func, span)
    
    # integrate part of odeinit
    def integrate(self, integrator: int) -> None:
        """
        docstring
        """
        self.flagIntegr = True
        super(WhiteDwarf, self).integrate(integrator)

    def getRadiusMass(self) -> tuple:
        """
        docstring
        """
        # implement some cut-off, maybe regime-dependent, i.e. for non-relativ
        # we have some rho<<rhoC, for relativistic where rho changes sign
        
        # find index of rho = 0
        if self.flagIntegr:
            index = np.searchsorted(-self.yOut[:,0],0)
            l = (3/(4*np.pi))**(1.0/3.0)
            self.Radius = index*l
            self.Mass = self.yOut[index-1,1]*self.rhoC
            # l - scaling const
            return self.Radius, self.Mass
        else:
            print("Integrate the eqn first")
            return None, None

    
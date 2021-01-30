"""
White dwarf class wrapper.
"""
import numpy as np
from scipy import constants as cs  # constants for the derivative equation

from . import derivatives, ode

class whiteDwarf(ode.ODEinit):
    """
    Provides a wrapper of the ODEinit class in the case of white dwarfs with
    some equation of state. Initializes an ODE with appropriate initial
    conditions while taking into account a normalization which leaves the ODE
    working with dimensionless quantities.

    Parameters
    ----------
    rhoC : float
        The density of matter in the small region around the center. In units
        of kg * m^(-3)
    span : np.ndarray
        The range of values of r to be calculated at. In normalized units to 
        cut down on computational time and improve calculation accuracy.
        Expects an array with step size 1 between members.
    regime : {1, 2, 3}, optional
        The regime indicates the choice of equation of state -> derivative, by
        default 1 - non-relativistic.

    Attributes
    ----------
    rhoC : float
        The density of matter in the small region around the center
    const1 : float
        Constant to be used in the derivative, depends on the `rhoC` value.
        Value after the normalization.
    const2 : float
        Second constant to be used in the derivative for the relativistic case,
        depends on `rhoC`. Value after the normalization.
    Radius : float
        Physical radius of the star. Has a value only after `getRadius()` has
        been called.
    Mass : float
        Mass of the star. Has a value only after `getRadius()` has been called.

    Methods
    -------
    getRadius
        Returns the tuple `(Radius, Mass)` of the star if the equation has been 
        integrated.

    Background
    ----------
    The differential equation is a coupled system of the density `rho` and mass
    `m` as functions of the distance from the centre `r`. These have some 
    dimensions in powers of kg and m. We transform the variables with some
    scaling constants so that the ODE solver works with dimensionless
    variables. The following choice of constants is made:
        rho = rhoC * theta,
        m = rhoC * mu,
        r = l * ksi,
    where rhoC is given as input by the user and `l^3*4*pi/3 = 1`. The choice 
    of l gives it a value on the order of 1, and we will choose it as our step
    size in r i.e. the step size in ksi is just 1. This is a convenient choice
    for normalization because of the initial condition on the mass:
    `m(l) = 4/3*pi*l^3*rhoC`. In this normalization, the initial condition
    becomes `mu(1) = 1`.
    """

    def __init__(self, rhoC: float, span: np.ndarray, regime: int=1) -> None:
        self.rhoC = rhoC
        # vector to be given as initial conditions, [rho, mass]
        init_condit = np.array([1.0, 1.0*(span[0]**3)])

        # constants in the derivative; computed here so that they are computed
        # only once rather than every time the derivative func is called
        self.const1 = -(2**(13.0/3))*cs.pi*cs.gravitational_constant *\
            cs.electron_mass*(cs.proton_mass**(5.0/3)) * \
            (rhoC**(1.0/3))*(cs.h**(-2.0))
        self.const2 = (3*rhoC/16/cs.pi/cs.proton_mass *
                       (cs.h/cs.c/cs.electron_mass)**3)**(2.0/3)

        # choose the equation of state and pass constants, prepares a function
        # to be passed to the constructor of ODEinit accepting (x, y) params
        if regime == 1:
            func = lambda a, b: derivatives.nonRelativGas(a, b, self.const1)
        elif regime == 2:
            func = lambda a, b: derivatives.relativGas(a, b, self.const1,
                                                         self.const2)
        elif regime == 3:
            func = lambda a, b: derivatives.ultraRel(a, b, self.const1)
        
        super(whiteDwarf, self).__init__(init_condit, func, span)

    def getRadiusMass(self) -> tuple:
        """
        Finds the radius and mass of the white dwarf, and returns them. Takes
        into account the normalization of the ODE. 

        The function scans `yOut[:,0]` column containing `rho(r)` values. We
        know that this is a decreasing function; the first instance where it 
        has a value <= 0 it where the star "ends".

        Returns
        -------
        tuple
            Returns a tuple `(Radius, Mass)`. Radius and Mass are calculated
            from `yOut` with the appropriate normalization constants. For
            Radius it is `l = (3/(4*pi))^(1/3)`, result is in m. For Mass it is
            `rhoC`, result is in kg.
        """

        # find index of rho = 0 (changing signs)
        if self.flagIntegrated:
            index = np.searchsorted(-self.yOut[:, 0], 0)
            # index is the position where we have yOut[index,:] ~ [0,0]

            l = (3/(4*np.pi))**(1.0/3.0)                # normalization const
            self.Radius = (index-1)*self.interval*l     # in m
            self.Mass = self.yOut[index-1, 1]*self.rhoC # in kg*m^(-3)
            return self.Radius, self.Mass
        else:
            print("Integrate the eqn first")
            return None, None

if __name__=="__main__":
    print(
        "This file contains declaration of a white dwarf class.")

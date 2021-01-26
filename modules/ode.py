"""
Implementation of a generic ODE integraror.
"""

import numpy as np
from . import integrators

class ODEinit(object):
    """
    Base class for a general ODE to be numerically integrated. It provides
    facilities to compute a value of some linear system given the ODE form as 
    `y' = f(x, y)` for some interval of values of `x` and initial conditions of 
    the vector `y`.

    Parameters
    ----------
    y0 : np.ndarray
        Initial conditions of the vector `y` at position `x = span[0]`
    deriv
        The function `f` in a functional form. Should accept two parameters at
        which to compute the derivative:
            x: float, the value of the independent variable;
            y: np.ndarray, the value of the dependent variable vector `y`.
    span : np.ndarray
        The interval values over which to compute the value of the vector `y`.

    Attributes
    ----------
    y0 : np.ndarray
        The initial state of the system. Passed at initalization.
    deriv
        The function `f` in a functional form. Passed at initalization.
    span : np.ndarray
        The interval of values to be integrated over. Passed at initalization.
        **Assumed to be equidistant!!**
    interval : float
        The size of the interval step; equal to `span[1] - span[0]`.
    yOut : np.ndarray
        The computed values of `y` after integration. Initialized as a martix
        of zeros; if integration terminates before the end of `span`, the rest
        of the points are left as zeros.
    flagIntegrated : bool
        A flag to indicate whether the integration has been done (and `yOut`
        filled) to be used by methods depending on having computed values.
    
    Methods
    -------
    integrate
        Integrates the differential equation.
    """

    def __init__(self, y0: np.ndarray, deriv, span: np.ndarray) -> None:
        self.y0 = y0
        self.deriv = deriv
        self.interval = span[1] - span[0]
        self.span = span

        # size of this is number of values to be computed x dimensions of y
        self.yOut = np.zeros((self.span.size, self.y0.size))
        
        # a flag taking note if the equation has been integrated
        self.flagIntegrated = False
    
    def integrate(self, integrator: int=3) -> None:
        """
        Integrates the equation using the function of the derivative `deriv`.
        User has the option to choose an integrator from the library, the
        default is a RK4 integrator. As it computes, it fills the `yOut` with 
        the computed values. Can terminate prematurely if the value passed to
        `deriv` is inappropriate; then the rest of the values are left as zero.

        Parameters
        ----------
        integrator : {1, 2, 3}, optional
            Choice of the integrator to be used given by the number:
                1: the Euler first order method;
                2: the Heun method, a second order method;
                3: the Runge-Kutta 4th order method.
        
        See Also
        --------
        modules.integrators
        """
        # choose an integrator
        self.integrator = integrators.index[integrator]

        # fill in the initial value of y
        self.yOut[0,:] = self.y0[:]

        #cycle does the integration
        for i in range(self.span.size-1):
            # the try exept handles the case where integration is impossible, 
            # i.e. when the value of an element of y is unphysical. deriv
            # decides when this is the case.
            try:
                # calculate the new value
                adder = self.integrator(
                    self.span[i], self.yOut[i,:], self.deriv, self.interval)
                # append new value
                self.yOut[i+1,:] = adder
            except ValueError:
                # ends the integration if it is impossible to integrate - Value
                # Error concerns the y-values
                break
        
        # to assert that the ODE has been integrated in funtions that use yOut.
        self.flagIntegrated = True

if __name__=="__main__":
    print(
        "This file contains declaration of a generic ODE class.")
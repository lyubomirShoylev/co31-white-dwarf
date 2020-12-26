"""
Hey there, this is a docstring.
"""
# Will include the definition of an ode
# Pass to it the initial value of y0-vector, the derivtion f-vector, and the range
# over which to return values. Will be able to select a given integration method
# to compare them later in the lab report.
# TODO documentation, the if __name__ == __main__ and so on

import numpy as np
from . import integrators

class ODEinit(object):
    """
    y0 - initial value
    """
    def __init__(self, y0: np.ndarray, deriv: function, range: np.ndarray) -> None:
        self.y0 = y0
        self.deriv = deriv
        self.interval = range[1] - range[0]
        self.range = range
    
    def integrate(self, integrator: int=3) -> None:
        """
        docstring
        """
        if integrator == 1:
            self.integrator = integrators.euler
        elif integrator == 2:
            self.integrator = integrators.heun
        elif integrator == 3:
            self.integrator = integrators.rk4
        else:
            # implement throwing error (at the end)
            pass

        self.yOut = np.zeros((self.range.size, self.y0.size))
        self.yOut[0,:] = self.y0[:]
        for i in range(1, self.range.size):
            adder = self.integrator(
                self.range[i], self.yOut[i-1,:], self.deriv, self.interval)
            self.yOut[i,:] = adder
        

    pass
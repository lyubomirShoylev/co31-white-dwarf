# Will include the definition of an ode
# Pass to it the initial value of y-vector, the function f-vector, and the range
# over which to return values. Will be able to select a given integration method
# to compare them later in the lab report.
# TODO documentation, the if __name__ == __main__ and so on

import numpy as np
# importing package like this since conda install does not play nicely
import integrators

class ODEinit(object):
    """
    docstring
    """
    def __init__(self, x: int, y: np.ndarray, func, interval: float,
                 range: np.ndarray) -> None:
        self.x = x
        self.y = y
        self.func = func
        self.interval = interval
        self.range = range
    
    def integrate(self, intType: int=3) -> None:
        """
        docstring
        """
        if intType == 1:
            self.integrator = integrators.euler
        elif intType == 2:
            self.integrator = integrators.heun
        elif intType == 3:
            self.integrator = integrators.rk4
        else:
            # implement throwing error (at the end)
            pass

        self.yOut = np.zeros((self.range.size, self.y.size))
        self.yOut[0,:] = self.y[:]
        for i in range(1, self.range.size):
            adder = self.integrator(
                self.range[i], self.yOut[i-1,:], self.func, self.interval)
            self.yOut[i,:] = adder
        

    pass
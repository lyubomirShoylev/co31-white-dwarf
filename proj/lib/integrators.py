"""
Integrators Library(`integrators.py`)
=====================================

This is a home to the different integrators used alongside the target of the 
exercise, namely Runge-Kutta 4th order (rk4) method. We implement two other 
methods to evaluate the advantages of the rk4 method, both in its accuracy and
precision.

Methods implemented
-------------------

    euler   Euler method - 1st order.
    heun    Heun method - a variant of a 2nd order.
    rk4     Runge-Kutta 4th order method.

Implementation notes
--------------------

All of the functions defined are to act on np.ndarray structures, therefore 
should be element-wise functions; all of the magic is done for us by numpy. 
The differential equation which they iterate is set up as `dy/dx = f(x, y)`, 
where y and f are N-dimensional vectors. Hence, all of the functions recieve 
four parameters:

    x : float, the point at which we start computing
    y : array_like, the values of the y-vector at x
    deriv : function, the derivative of y to be computed at some (x, y) coords
    h : float, the interval size

All of the functions return the value of y for the next place in the
integration range. How we determine its value, or more precisely the increment
from the previous value, is the difference between these methods.
"""
# TODO improve memory/calc cycles
import numpy as np

def euler(x: float, y: np.ndarray, deriv: function, h: float) -> np.ndarray:
    """
    Compute an iteration using Euler's method: a 1st order method.

    This function computes an iteration in the numerical integration of an ODE
    of the form `dy/dx = f(x, y)` using the first order Euler method:
    `y(x + h) = y(x) + h*f(x, y(x))`, where h is the size of the step in the 
    x-coordinate.

    Parameters
    ----------
    x : float
        Starting coordinate in x.
    y : ndarray
        Starting coordinate in y. In general can be an N-dimensional array.
    deriv : function
        A function which computes the derivative of the y-vector given the 
        x and y coords.
    h : float
        The step size in x.
    
    Returns
    -------
    ndarray
        The returned value is the approximation of y(x + h) using the Euler
        algoritm.

    """
    # TODO include examples
    return y + h*deriv(x,y)

def heun(x: float, y: np.ndarray, deriv: function, h: float) -> np.ndarray:
    """
    Compute an iteration using Heun's method, a kind of 2nd order method.

    This function computes an iteration in the numerical integration of an ODE
    of the form `dy/dx = f(x, y)` using the second order Heun method:
    `y(x + h) = y(x) + 0.5*h*(f(x, y(x)) + f(x + h, y + h*f(x, y)))`, where h 
    is the size of the step in the x-coordinate. This is a predictor-corrector
    method, and uses the prediction of the slope at `x + h` to correct the 
    final calculation of the slope to be added.

    Parameters
    ----------
    x : float
        Starting coordinate in x.
    y : ndarray
        Starting coordinate in y. In general can be an N-dimensional array.
    deriv : function
        A function which computes the derivative of the y-vector given the 
        x and y coords.
    h : float
        The step size in x.

    Returns
    -------
    np.ndarray
        The returned value is the approximation of y(x + h) using the Heun
        algoritm.
    """
    return y + 0.5*h*(deriv(x, y) + deriv(x + h, y + h*deriv(x,y)))

def rk4(x: float, y: np.ndarray, deriv: function, h: float) -> np.ndarray:
    """
    Compute an iteration using a 4th order Runge-Kutta method.

    This function computes an iteration in the numerical integration of an ODE
    of the form `dy/dx = f(x, y)` using a fourth order Runge-Kutta method.

    Parameters
    ----------
    x : float
        Starting coordinate in x.
    y : ndarray
        Starting coordinate in y. In general can be an N-dimensional array.
    deriv : function
        A function which computes the derivative of the y-vector given the 
        x and y coords.
    h : float
        The step size in x.

    Returns
    -------
    np.ndarray
        The returned value is the approximation of y(x + h) using the 4th order
        Runge-Kutta algoritm.
    """
    # TODO reduce the calculation cycle per NumMeht book
    k1 = h*deriv(x,y)
    k2 = h*deriv(x + 0.5*h, y + 0.5*k1)
    k3 = h*deriv(x + 0.5*h, y + 0.5*k2)
    k4 = h*deriv(x + h, y + k3)

    return y + (k1 + k4)/6.0 + (k2 + k3)/3.0

if __name__=="__main__":
    print(
        "This is a module home to several integrators to be used in solving \
ODEs: Euler, Heun, Runge-Kutta4.")
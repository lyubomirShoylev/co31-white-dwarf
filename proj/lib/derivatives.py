"""
# a file containing some derivative functions that are to be used by an ODE as
# the derivative. Include the functions for a white-dwarf in the different
# regimes - relativistic and non-relativistic
Description: collection of functions with which to test/compute
"""
# TODO to implement a diff eqn ~ second power to evaluate the error in a 
# comparable eqn to the one we are solving

import numpy as np

def SHO(x: float, y: np.ndarray) -> np.ndarray:
    """
    Function of the derivative for the simple harmonic oscillator written as a
    system of linear ODEs.

    Parameters
    ----------
    x : float
        Value of the independent variable in the ODE.
    y : np.ndarray
        Value of the dependent variable in the ODE. Two element vector
        `[z', z]`, where the SHO ODE is `z''(x) + z(x) = 0`.

    Returns
    -------
    np.ndarray
        The value of the derivative at (x, y)

    Notes
    -----
    The equation `z''(x) + z(x) = 0` is written using `p = z'` in the form:
    `y' = [p, z]' = [-z, p]`. The funtion returns the latter vector.
    """
    return np.array([-1.0*y[1], y[0]])

def nonRelativGas(x: float, y: np.ndarray, const: float) -> np.ndarray:
    """
    Function of the derivative for the system of coupled equations
    `y = [rho, m](x)` in the non-relativistic case. An additional argument
    `const` is passed to save computational time - it is calculated only once
    in the ODE definition, and called as value to be used in the computations.

    Parameters
    ----------
    x : float
        Value of the independent variable in the ODE.
    y : np.ndarray
        Value of the dependent variable in the ODE. *Two elements only.*
    const: float
        The scaling constant used in the definition. 

    Returns
    -------
    np.ndarray
        The value of the derivative at (x, y). Look at Notes for info on the
        functional form.
    
    Raises
    ------
    ValueError
        If the value `y[0]` < 0, the computation is discarded on physical 
        grounds - cannot have negative matter density. Raises an exception
        propagated by the integrator to be handled in the .integration method.
    
    Notes
    -----
    The functional form is determined by the equation of state in the
    non-relativistic case, where `pressure = someConst * rho^(2/3)`.The final
    form: `[rho, m]' = [const1*m*rho^(1/3)/x^2, 3*x^2*rho]`.
    """
    
    # need y[0] >= 0 to be exponentiated apart from physical grounds
    if y[0] < 0:
        raise ValueError
    return  np.array([const*y[1]*(y[0]**(1.0/3))*(x**(-2.0)), 
                        3*(x**2)*y[0]])

def relativGas(x: float, y: np.ndarray, const1: float ,const2: float) -> np.ndarray:
    """
    Function of the derivative for the system of coupled equations
    `y = [rho, m](x)` in the relativistic case. Two additional arguments 
    `const1` and `const2` are passed to save on computational time - they are
    calculated only once in the ODE definition, and called as value to be used
    in the computations.

    Parameters
    ----------
    x : float
        Value of the independent variable in the ODE.
    y : np.ndarray
        Value of the dependent variable in the ODE. *Two elements only.*
    const1: float
        One of the scaling constants, used in the derivative of rho.
    const2 : float
        The second scaling constant, used in the relativistic correction.

    Returns
    -------
    np.ndarray
        The value of the derivative at (x, y). Look at Notes for info on the
        functional form.

    Raises
    ------
    ValueError
        If the value `y[0]` < 0, the computation is discarded on physical 
        grounds - cannot have negative matter density. Raises an exception
        propagated by the integrator to be handled in the .integration method.

    Notes
    -----
    The functional form is determined by the equation of state in the
    relativistic case, where `pressure = someConst*rho^(2/3)*relCorr`.The
    relativistic correction is `relCorr = sqrt(1+const2*rho^(2/3))^(-1)`.
    The final form: `[rho, m]' = [const1*m*rho^(1/3)*relCorr/x^2, 3*x^2*rho]`.
    """

    # need y[0] >= 0 to be exponentiated apart from physical grounds
    if y[0] < 0:
        raise ValueError

    return np.array([const1*y[1]*(y[0]**(1.0/3))*(x**(-2.0))*
                        (1+const2*(y[0]**(2.0/3)))**(0.5), 3*(x**2)*y[0]])

# XXX decide what to do with this - is it only for theory or computational?
def ultraRel(x: float, y: np.ndarray, const: float) -> np.ndarray:
    """
    docstring - placeholder
    """
    if y[0] < 0:
        # need y[0] >= 0 to be exponentiated (on physical grounds as well)
        raise ValueError
    out = np.array([0, 0])
    return out

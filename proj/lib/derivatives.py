# a file containing some derivative functions that are to be used by an ODE as
# the derivative. Include the functions for a white-dwarf in the different
# regimes - relativistic and non-relativistic
import numpy as np
def SHO(x: float, y: np.ndarray) -> np.ndarray:
    """
    docstring
    """
    return np.array([-1.0*y[1], y[0]])

def someODE(x: float, y: float) -> np.ndarray:
    """
    docstring
    """
    return y*(2/(np.exp(x)+1)-1)

def someODEsln(x: float) -> float:
    """
    docstring
    analytical solution to the ODE in someODE
    """
    return 12*np.exp(x)*((np.exp(x)+1)**(-2))

def nonRelativGas(x: float, y: np.ndarray, scalar: float) -> np.ndarray:
    """
    Eqn of the non-relativ. gas

    Parameters
    ----------
    x : float
        [description]
    y : np.ndarray
        [description]

    Returns
    -------
    np.ndarray
        [description]
    """
    out = np.array([scalar*y[1]*(y[0]**(1.0/3))*(x**(-2.0)), 3*(x**2)*y[0]])
    return out

def relativGas(parameter_list):
    """
    docstring - placeholder
    """
    return 1

def ultraRel(parameter_list):
    """
    docstring - placeholder
    """
    return 1
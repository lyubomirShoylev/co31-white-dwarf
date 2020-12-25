# describe several integrator methods to compare results/accuracu/efficiency
# later. the functions should be "element-wise" since we want them to play
# nicely with numpy arrays. recieve x, y-vector, function f-vector, interval h.
# return the y-vector at x+h (i.e. the next step)
# TODO improve memory/calc cycles
# TODO documentation, the if __name__ == __main__ and so on

def euler(x, y, func, h):
    """
    docstring
    """
    return y + h*func(x,y)

def heun(x, y, func, h):
    """
    docstring
    """
    return y + h*(func(x, y) + func(x + h, y + h*func(x,y)))/2.0

def rk4(x, y, func, h):
    """
    docstring
    """
    # TODO reduce the calculation cycle per NumMeht book
    k1 = h*func(x,y)
    k2 = h*func(x + 0.5*h, y + 0.5*k1)
    k3 = h*func(x + 0.5*h, y + 0.5*k2)
    k4 = h*func(x + h, y + k3)

    return y + (k1 + k4)/6.0 + (k2 + k3)/3.0
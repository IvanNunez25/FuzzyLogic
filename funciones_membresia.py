import numpy as np

def membresia_booleana (x, x0):
    if x <= x0:
        return 1

    return 0

def membresia_booleana_inversa (x, x0):
    if x <= x0:
        return 0

    return 1

def membresia_de_grado (x, x0, x1):
    if x <= x0:
        return 0
    elif x > x0 and x <= x1:
        return 0 #pendiente
    
    return 1

def membresia_de_grado_inversa (x, x0, x1):
    if x <= x0:
        return 1
    elif x > x0 and x <= x1:
        return 0 #pendiente
    
    return 0

def membresia_triangular (x, x0, x1, x2):
    if x <= x0:
        return 0
    elif x > x0 and x <= x1:
        return 0 #pendiente
    elif x > x1 and x <= x2:
        return 0 #pendiente

    return 0

def trapezoidal (x, x0, x1, x2, x3):
    if x <= x0:
        return 0
    elif x > x0 and x <= x1:
        pendiente = 1 / (x1 - x0)
        return pendiente * (x - x0)
    elif x > x1 and x <= x2:
        return 1
    elif x > x2 and x <= x3:
        pendiente = -1 / (x3 - x2)
        return 1 + pendiente * (x - x2)
    
    return 0

def pi_shaped (x, a, b, c, d):
    
    """
    Función pi-shaped tomada de la documentación de fuzzy:
    
    Pi-function fuzzy membership generator.

    Parameters
    ----------
    x : 1d array
        Independent variable.
    a : float
        Left 'foot', where the function begins to climb from zero.
    b : float
        Left 'ceiling', where the function levels off at 1.
    c : float
        Right 'ceiling', where the function begins falling from 1.
    d : float
        Right 'foot', where the function reattains zero.

    Returns
    -------
    y : 1d array
        Pi-function.

    """
    y = np.ones(len(x))
    assert a <= b and b <= c and c <= d, 'a <= b <= c <= d is required.'

    idx = x <= a
    y[idx] = 0

    idx = np.logical_and(a <= x, x <= (a + b) / 2.)
    y[idx] = 2. * ((x[idx] - a) / (b - a)) ** 2.

    idx = np.logical_and((a + b) / 2. < x, x <= b)
    y[idx] = 1 - 2. * ((x[idx] - b) / (b - a)) ** 2.

    idx = np.logical_and(c <= x, x < (c + d) / 2.)
    y[idx] = 1 - 2. * ((x[idx] - c) / (d - c)) ** 2.

    idx = np.logical_and((c + d) / 2. <= x, x <= d)
    y[idx] = 2. * ((x[idx] - d) / (d - c)) ** 2.

    idx = x >= d
    y[idx] = 0

    return y

def generalized_bell(x, a, b, c):
    
    """
    Generalized Bell function fuzzy membership generator.

    Parameters
    ----------
    x : 1d array
        Independent variable.
    a : float
        Bell function parameter controlling width. See Note for definition.
    b : float
        Bell function parameter controlling center. See Note for definition.
    c : float
        Bell function parameter controlling slope. See Note for definition.

    Returns
    -------
    y : 1d array
        Generalized Bell fuzzy membership function.

    Notes
    -----
    Definition of Generalized Bell function is:

        y(x) = 1 / (1 + abs([x - c] / a) ** [2 * b])

    """
    return 1. / (1. + np.abs((x - c) / a) ** (2 * b))
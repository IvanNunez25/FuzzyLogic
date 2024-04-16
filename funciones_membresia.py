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

def membresia_trapezoidal (x, x0, x1, x2, x3):
    if x <= x0:
        return 0
    elif x > x0 and x <= x1:
        return 0 #pendiente
    elif x > x1 and x <= x2:
        return 1
    elif x > x2 and x <= x3:
        return 0 #pendiente
    
    return 0
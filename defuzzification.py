def centroide(membership_function, universe_of_discourse):
    total = 0
    i = 0
    for mf in membership_function:
        area = mf * universe_of_discourse[i]
        i += 1
        
        total += area
    
    return total / sum(membership_function)

membership_function = [0.5, 2.0, 0.05, 0.15, 0.15, 0.15]
universe_of_discourse = [2.333, 5, 7.166, 7.25, 7.75, 8.333]

centroid = centroide(membership_function, universe_of_discourse)
print("El centroide de la función de membresía es: ", round(centroid, 10))

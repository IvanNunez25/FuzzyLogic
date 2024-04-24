def centroide(membership_function, universe_of_discourse):
    total = 0
    i = 0
    for mf in membership_function:
        area = mf * universe_of_discourse[i]
        i += 1
        
        total += area
    
    return total / sum(membership_function)

def centroid_defuzzification(membership_function, universe_of_discourse):
    # Calcula el área bajo la curva de membresía utilizando la regla del punto medio
    total_area = 0
    centroid_numerator = 0
    
    for i in range(len(membership_function) - 1):
        x1 = universe_of_discourse[i]
        x2 = universe_of_discourse[i + 1]
        y1 = membership_function[i]
        y2 = membership_function[i + 1]
        
        # Regla del punto medio para calcular el área del trapecio
        area = (x2 - x1) * (y1 + y2) / 2
        
        total_area += area
        centroid_numerator += (x1 + x2) * area / 2
    
    # Calcula el centroide dividiendo el numerador entre el área total
    centroid = centroid_numerator / total_area
    
    return centroid

# Ejemplo de uso
membership_function = [0.5, 2.0, 0.05, 0.15, 0.15, 0.15]
universe_of_discourse = [2.333, 5, 7.166, 7.25, 7.75, 8.333]
# universe_of_discourse = range(len(membership_function))

#centroid = centroid_defuzzification(membership_function, universe_of_discourse)
centroid = centroide(membership_function, universe_of_discourse)
print("El centroide de la función de membresía es:", round(centroid, 6))

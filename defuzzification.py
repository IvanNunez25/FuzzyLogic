def centroide(membership_function, universe_of_discourse):
    total = 0
    i = 0
    for mf in membership_function:
        area = mf * universe_of_discourse[i]
        i += 1
        
        total += area
    
    return total / sum(membership_function)

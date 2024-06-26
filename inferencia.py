import random

'''

if <condicion> then
    <analisis>

condicion -> antecedente
analisis -> consecuente

    -- SOLO EXISTEN 3 OPERADORES LÓGICOS --

AND difuso: El resultado de la expresión es el menor de los dos operandos

    AND ( p1, p2 ) -> min ( p1, p2 )
    
OR difuso: El resultado de la operación es el mayor de los dos operandos

    OR ( p1, p2 ) -> max ( p1, p2 )

NOT: solo restamos a uno el valor del operando que le corresponde 
    
    NOT ( p1 ) -> 1 - p1
    


 -- SALIDAS --
 
 -> tiempo_lavado
 corto      medio       largo
 0          35  62.5    100
 
 -> temperatura
 fria       templada    caliente
 0          35  65      100
 
 -> secado
 corto      medio       largo
 0          35  65      100
 
 -> temperatura
 bajo       media       alta
 0          35  65      100
 
 -> temperatura
 bajo       medio       alto
 0          40  60      100

'''

tiempo_lavado = []
temperatura = []
tiempo_secado = []
velocidad = []
nivel_agua = []
list_rules = []

def fuzzy_and ( num1, num2 ):
    return min( num1, num2 )

def fuzzy_or ( num1, num2 ):
    return max( num1, num2 )

def fuzzy_not ( num ):
    return 1 - num

def activated_rule ( lavado, temp, secado, vel, agua ):
    
    if lavado == 1:
        tiempo_lavado.append( random.randint( 62, 100 ) / 100 )
    elif lavado == 2:
        tiempo_lavado.append( random.randint( 35, 62 ) / 100 )
    else:
        tiempo_lavado.append( random.randint( 0, 35 ) / 100 )
        
    if temp == 1:
        temperatura.append( random.randint( 65, 100 ) / 100 )
    elif temp == 2:
        temperatura.append( random.randint( 35, 65) / 100 )
    else:
        temperatura.append( random.randint( 0, 35 ) / 100 )
        
    if secado == 1:
        tiempo_secado.append( random.randint( 65, 100 ) / 100 )
    elif secado == 2:
        tiempo_secado.append( random.randint( 35, 65) / 100 )
    else:
        tiempo_secado.append( random.randint( 0, 35 ) / 100 )
        
    if vel == 1:
        velocidad.append( random.randint( 65, 100 ) / 100 )
    elif vel == 2:
        velocidad.append( random.randint( 35, 65) / 100 )
    else:
        velocidad.append( random.randint( 0, 35 ) / 100 )
        
    if agua == 1:
        nivel_agua.append( random.randint( 60, 100 ) / 100 )
    elif agua == 2:
        nivel_agua.append( random.randint( 40, 60) / 100 )
    else:
        nivel_agua.append( random.randint( 0, 40 ) / 100 )
    

def inferencia ( tipo_tela, tipo_suciedad, nivel_carga ):
    
    # Regla 1
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 3, 3, 2, 1 )
        rules( 1, 0, 0, 0, 1, 3, 3, 2, 1 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 2, 2, 2, 2 )
        rules( 2, 0, 0, 1, 1, 2, 2, 2, 2  )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 2, 3, 2, 1 )
        rules( 3, 0, 0, 2, 1, 2, 3, 2, 1 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
        rules( 4, 0, 1, 0, 2, 2, 3, 2, 3)
     
    # Regla 5   
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 2, 2, 2, 2 )
        rules( 5, 0, 1, 1, 2, 2, 2, 2, 2 )
        
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
        rules( 6, 0, 1, 2, 2, 2, 3, 2, 3 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        rules( 7, 0, 2, 0, 1, 1, 1, 1, 1 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        rules( 8, 0, 2, 1, 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        rules( 9, 0, 2, 2, 1, 1, 3, 1, 3 )
        
    # Regla 10
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 1, 1, 1, 1 )
        rules( 10, 1, 0, 0, 3, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 1, 2, 1, 2 )
        rules( 11, 1, 0, 1, 3, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 1, 3, 1, 3 )
        rules( 12, 1, 0, 2, 3, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 1, 1, 1, 1 )
        rules( 13, 1, 1, 0, 2, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 1, 2, 1, 2 )
        rules( 14, 1, 1, 1, 2, 1, 2, 1, 2 )
   
    # Regla 15     
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 1, 3, 1, 3 )
        rules( 15, 1, 1, 2, 2, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        rules( 16, 1, 2, 0, 1, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        rules( 17, 1, 2, 1, 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        rules( 18, 1, 2, 2, 1, 1, 3, 1, 3 )
    
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 1, 1, 2, 1 )
        rules( 19, 2, 0, 0, 3, 1, 1, 2, 1 )
        
    # Regla 20
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 1, 2, 2, 2 )
        rules( 20, 2, 0, 1, 3, 1, 2, 2, 2 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 1, 3, 2, 3 )
        rules( 21, 2, 0, 2, 3, 1, 3, 2, 3 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 1, 1, 1, 1 )
        rules( 22, 2, 1, 0, 2, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 1, 2, 1, 2 )
        rules( 23, 2, 1, 1, 2, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 1, 3, 1, 3 )
        rules( 24, 2, 1, 2, 2, 1, 3, 1, 3 )
        
    # Regla 25
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        rules( 25, 2, 2, 0, 1, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        rules( 26, 2, 2, 1, 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        rules( 27, 2, 2, 2, 1, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 2, 1, 3, 1 )
        rules( 28, 3, 0, 0, 3, 2, 1, 3, 1 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 2, 2, 3, 2 )
        rules( 29, 3, 0, 1, 3, 2, 2, 3, 2 )
        
    # Regla 30
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 2, 3, 3, 3 )
        rules( 30, 3, 0, 2, 3, 2, 3, 3, 3 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 2, 1, 2, 1 )
        rules( 31, 3, 1, 0, 2, 2, 1, 2, 1 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 2, 2, 2, 2 )
        rules( 32, 3, 1, 1, 2, 2, 2, 2, 2 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
        rules( 33, 3, 1, 2, 2, 2, 3, 2, 3 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        rules( 34, 3, 2, 0, 1, 1, 1, 1, 1 )
        
    # Regla 35
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        rules( 35, 3, 2, 1, 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        rules( 36, 3, 2, 2, 1, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 3, 1, 3, 1 )
        rules( 37, 4, 0, 0, 3, 3, 1, 3, 1 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 3, 2, 3, 2 )
        rules( 38, 4, 0, 1, 3, 3, 2, 3, 2 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 3, 3, 3, 3 )
        rules( 39, 4, 0, 2, 3, 3, 3, 3, 3 )
        
    # Regla 40
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 2, 1, 2, 1 )
        rules( 40, 4, 1, 0, 2, 2, 1, 2, 1 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 2, 2, 2, 2 )
        rules( 41, 4, 1, 1, 2, 2, 2, 2, 2 )
    
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
        rules( 42, 4, 1, 2, 2, 2, 3, 2, 3 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        rules( 43, 4, 2, 0, 1, 1, 1, 1, 1)
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        rules( 44, 4, 2, 1, 1, 1, 2, 1, 2 )
    
    # Regla 45
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        rules( 45, 4, 2, 2, 1, 1, 3, 1, 3 )
    
    return tiempo_lavado.copy(), temperatura.copy(), tiempo_secado.copy(), velocidad.copy(), nivel_agua.copy()

def rules ( n_rule, tela, suciedad, carga, lavado, temp, secado, vel, agua ):
    
    match tela:
        case 0: tipo_tela = "piel"
        case 1: tipo_tela = "seda"
        case 2: tipo_tela = "lana"
        case 3: tipo_tela = "algodon"
        case 4: tipo_tela = "poliester"
        
    match suciedad:
        case 0: tipo_suciedad = "manchas_comida"
        case 1: tipo_suciedad = "grasa"
        case 2: tipo_suciedad = "tierra"
        
    match carga:
        case 0: nivel_carga = "ligero"
        case 1: nivel_carga = "medio"
        case 2: nivel_carga = "pesado"
        
    if lavado == 1: t_lavado = "largo"
    elif lavado == 2: t_lavado = "medio"
    else: t_lavado = "corto"
        
    if temp == 1: tempe = "caliente"
    elif temp == 2: tempe = "templada"
    else: tempe = "frio"
        
    if secado == 1: t_secado = "largo"
    elif secado == 2: t_secado = "medio"
    else: t_secado = "corto"
        
    if vel == 1: velo = "alta"
    elif vel == 2: velo = "media"
    else: velo = "baja"
        
    if agua == 1: n_agua = "alto"
    elif agua == 2: n_agua = "medio"
    else: n_agua = "bajo"
        
    
    regla = f"Regla {n_rule} if tipo_tela = { tipo_tela } AND tipo_suciedad = {tipo_suciedad} AND nivel_carga = {nivel_carga} \nthen tiempo_lavado = {t_lavado}, temperatura = {tempe}, temp_secado = {t_secado}, velocidad = {velo}, nivel_agua = {n_agua}"
    list_rules.append(regla)
    
def getRules ():
    return list_rules.copy()
    

def clear ():
    tiempo_lavado.clear()
    temperatura.clear()
    tiempo_secado.clear()
    velocidad.clear()
    nivel_agua.clear()
    list_rules.clear()
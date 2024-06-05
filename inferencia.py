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
        tiempo_lavado.append( random.randint( 35 ) / 100 )
        
    if temp == 1:
        temperatura.append( random.randint( 65, 100 ) / 100 )
    elif temp == 2:
        temperatura.append( random.randint( 35, 65) / 100 )
    else:
        temperatura.append( random.randint( 35 ) / 100 )
        
    if secado == 1:
        tiempo_secado.append( random.randint( 65, 100 ) / 100 )
    elif secado == 2:
        tiempo_secado.append( random.randint( 35, 65) / 100 )
    else:
        tiempo_secado.append( random.randint( 35 ) / 100 )
        
    if vel == 1:
        velocidad.append( random.randint( 65, 100 ) / 100 )
    elif vel == 2:
        velocidad.append( random.randint( 35, 65) / 100 )
    else:
        velocidad.append( random.randint( 35 ) / 100 )
        
    if agua == 1:
        nivel_agua.append( random.randint( 60, 100 ) / 100 )
    elif agua == 2:
        nivel_agua.append( random.randint( 40, 60) / 100 )
    else:
        nivel_agua.append( random.randint( 40 ) / 100 )
    

def inferencia ( tipo_tela, tipo_suciedad, nivel_carga ):
    
    # Regla 1
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 3, 3, 2, 1 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 2, 2, 2, 2 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 2, 3, 2, 1 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
     
    # Regla 5   
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 2, 2, 2, 2 )
        
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
    
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[0], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        
    # Regla 10
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 1, 2, 1, 2 )
   
    # Regla 15     
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[1], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
    
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 1, 1, 2, 1 )
        
    # Regla 20
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 1, 2, 2, 2 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 1, 3, 2, 3 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 1, 3, 1, 3 )
        
    # Regla 25
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[2], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 2, 1, 3, 1 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 2, 2, 3, 2 )
        
    # Regla 30
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 2, 3, 3, 3 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 2, 1, 2, 1 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 2, 2, 2, 2 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        
    # Regla 35
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
        
    if fuzzy_and( tipo_tela[3], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[0], nivel_carga[0] ) ) > 0:
        activated_rule( 3, 3, 1, 3, 1 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[0], nivel_carga[1] ) ) > 0:
        activated_rule( 3, 3, 2, 3, 2 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[0], nivel_carga[2] ) ) > 0:
        activated_rule( 3, 3, 3, 3, 3 )
        
    # Regla 40
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[1], nivel_carga[0] ) ) > 0:
        activated_rule( 2, 2, 1, 2, 1 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[1], nivel_carga[1] ) ) > 0:
        activated_rule( 2, 2, 2, 2, 2 )
    
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[1], nivel_carga[2] ) ) > 0:
        activated_rule( 2, 2, 3, 2, 3 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[2], nivel_carga[0] ) ) > 0:
        activated_rule( 1, 1, 1, 1, 1 )
        
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[2], nivel_carga[1] ) ) > 0:
        activated_rule( 1, 1, 2, 1, 2 )
    
    # Regla 45
    if fuzzy_and( tipo_tela[4], fuzzy_and( tipo_suciedad[2], nivel_carga[2] ) ) > 0:
        activated_rule( 1, 1, 3, 1, 3 )
    
    return tiempo_lavado, temperatura, tiempo_secado, velocidad, nivel_agua
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

'''
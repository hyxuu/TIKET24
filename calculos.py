def calcularCuota(monto, interesanual, meses):
    tasa_mensual =  interesanual / 100 /12
    cuota= (monto * tasa_mensual * (1 + tasa_mensual) ** meses) / ((1 + tasa_mensual) ** meses - 1)
    return cuota

def determinarResultadosIMC(imc):
    if 0 <= imc < 16:
        return "Delgadez severa"
    elif 16 <= imc < 17:
        return "Delgadez moderada"
    elif 17 <= imc < 18.5:
        return "Delgadez leve"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado 1"
    elif 35 <= imc < 40:
        return "Obesidad Grado 2"
    elif imc >= 40:
        return "Obesidad Grado 3"
    else:
        return "IMC fuera de rango"

from datetime import datetime
def calcularEdad(anioNacimiento):
    
    anioActual = datetime.now().year
    if anioNacimiento < 0 or anioNacimiento > anioActual:
        return -1  
    edad = anioActual - anioNacimiento
    return edad        
        
def encontrarMayor(valor1, valor2, valor3):
    mayorActual = valor1
    if valor2 > mayorActual:
        mayorActual = valor2
    if valor3 > mayorActual:
        mayorActual = valor3
    
    return mayorActual
    
def encontrarMenor(valor1, valor2, valor3, valor4):
    menorActual = valor1
    if valor2 < menorActual:
        menorActual = valor2
    if valor3 < menorActual:
        menorActual = valor3
    if valor4 < menorActual:
        menorActual = valor4
    
    return menorActual

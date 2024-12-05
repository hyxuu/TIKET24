def calcularCuota(monto, interesanual, meses):
    tasa_mensual =  interesanual / 100 /12
    cuota= (monto * tasa_mensual * (1 + tasa_mensual) ** meses) / ((1 + tasa_mensual) ** meses - 1)
    return cuota
def encontrarMenor(valor1, valor2, valor3, valor4):
    menorActual = valor1
    if valor2 < menorActual:
        menorActual = valor2
    if valor3 < menorActual:
        menorActual = valor3
    if valor4 < menorActual:
        menorActual = valor4
    
    return menorActual

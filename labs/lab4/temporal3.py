# Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : Ricardo Rivera Rojas 
# Fecha : 2022.10.05
# Editado 2022.10.05

contador=0
valor=0
while True:
    numero=input("introduzca el numero: ")
    if numero=="fin":
        break
    try:
        valor=valor+int(numero)
        contador=contador+1
    except:
        print("Entrada Inválida")
print("la suma de los numeros es: ", valor)
print("el conteo de los numeros es: ", contador)
print("el promedio de los numeros es: ", valor/contador)





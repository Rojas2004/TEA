# Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : Ricardo Rivera Rojas 
# Fecha : 2022.09.29
# Editado 2022.09.29

cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1
final = len(cadena)
print(inicio, final)
print(cadena[inicio:final])


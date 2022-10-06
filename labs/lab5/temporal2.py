# Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : Ricardo Rivera Rojas 
# Fecha : 2022.09.29
# Editado 2022.09.29

try:
  entrada = input("ingrese el nombre del archivo: ")
  archivo = open(entrada)
  for linea in archivo:
    print(linea.upper())
except:
     print("error, no existe el archivo")
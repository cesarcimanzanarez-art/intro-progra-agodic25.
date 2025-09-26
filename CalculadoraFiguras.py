#from math import * #Nos importamos toda la librería
#from math import sqrt,pi #aquí importamos la función de la raiz cuadrada y el valor de pi
from math import sqrt,pi #aquí importamos solo el valor de pi

print("-----Bienvenida a mi Calculadora de Figuras------")
print("Menú de figuras")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")

figura = input("Figura (1-6) ")

print("---Menu de opciones----")
print("1. Cálculo de áreas")
print("2. Cálculo de Volumen")
print("3. C{alculo de ambos")
print("4. Salir")

opcion = input("opción (1-4):")

if opcion == "1": # Este if aninado 
    if figura == "1":
       lado = float(input("Lado (cm):"))
       areaCubo = 6*lado**2
       print(f"El área del cubo es: {areaCubo:.2}")
    elif figura == "2":
       largobase = float(input("Largo de la base (cm):"))
       anchobase = float(input("Ancho de la base (cm):"))
       altura = float(input("altura (cm):"))
       areabase = largobase*anchobase
       perimetrobase = 2*anchobase+2*largobase
       areaPrisma = 2*areabase+altura*perimetrobase
       print(f"El área del cubo es: {areaPrisma:.2}")
    elif figura == "3":
        pass
    elif figura == "4":
        pass
    elif figura == "5":
        pass
    elif figura == "6":
        pass
    else:
        print("No conozco esa figura. ")
elif opcion == "2":
    if figura == "1":
       lado = float(input("Lado (cm):"))
       volumenCubo = lado**3
       print(f"El volumen del cubo es: {volumenCubo:.2}")
    elif figura == "2":
       largobase = float(input("Largo de la base (cm):"))
       anchobase = float(input("Ancho de la base (cm):"))
       altura = float(input("altura (cm):"))
       areabase = largobase*anchobase
       volumenPrisma = areabase+altura
       print(f"El volumen del cubo es: {volumenPrisma:.2}")
    elif figura == "3":
        pass
    elif figura == "4":
        pass
    elif figura == "5":
        pass
    elif figura == "6":
        pass
    else:
        print("No conozco esa figura. ")

elif opcion == "3":
    if figura == "1": #Este if aninado controla la figura para calcular ambos.
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2}")
    elif figura == "2":
       largobase = float(input("Largo de la base (cm):"))
       anchobase = float(input("Ancho de la base (cm):"))
       altura = float(input("altura (cm):"))
       areabase = largobase*anchobase
       perimetrobase = 2*anchobase+2*largobase
       areaPrisma = 2*areabase+altura*perimetrobase
       print(f"El área del cubo es: {areaPrisma:.2}")
       volumenPrisma = areabase+altura
       print(f"El volumen del cubo es: {volumenPrisma:.2}")
    elif figura == "3":
        pass
    elif figura == "4":
        pass
    elif figura == "5":
        pass
    elif figura == "6":
        pass
    else:
        print("No conozco esa figura. ")
elif opcion == "4":
    print("Hastal luego =)")
else:
    print("Opción incorrecta, adiós. =D")
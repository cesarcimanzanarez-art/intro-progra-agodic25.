print("-----Bienvenido al Cajero Automático------")
print("Menú de Opciones")
print("1. Consultar Saldo")
print("2. Retirar Efectivo")
print("3. Depositar Efectivo")
print("4. Salir")

saldo= 1000

opcion = input("Opciones (1-4) ")

if opcion == "1":
    print("Tu saldo es:", saldo)
if opcion == "2":
    print("Cantidad que deseas retirar")
    print("1. $500")
    print("2. $1,000")
    print("3. $2,000")
    print("4. $3,000")
    opcion = input("Opciones (1-4) ")
    if opcion == "1":
       monto = 500
       if monto <= saldo:
          saldo_actual = saldo-monto
          print(f"Tu nuevo saldo es: {saldo_actual}") 
       if monto > saldo:
          print(f"Tu saldo es insuficiente") 
    if opcion == "2":
       monto = 1000
       if monto <= saldo:
          saldo_actual = saldo-monto
          print(f"Tu nuevo saldo es: {saldo_actual}") 
       if monto > saldo:
          print(f"Tu saldo es insuficiente") 
    if opcion == "3":
       monto = 2000
       if monto <= saldo:
          saldo_actual = saldo-monto
          print(f"Tu nuevo saldo es: {saldo_actual}") 
       if monto > saldo:
          print(f"Tu saldo es insuficiente") 
    if opcion == "4":
       monto = 3000
       if monto <= saldo:
          saldo_actual = saldo-monto
          print(f"Tu nuevo saldo es: {saldo_actual}") 
       if monto > saldo:
          print(f"Tu saldo es insuficiente") 
if opcion == "3":
   monto_depositado = float(input("Ingrese el monto a depositar: $ "))
   nuevo_monto = saldo + monto_depositado
   print(f"Tu nuevo saldo es", nuevo_monto)
if opcion == "4":
   print("No olvides recoger tu tarjeta, Regresa Pronto")
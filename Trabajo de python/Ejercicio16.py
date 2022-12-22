acu = 0.0
ahorros = 0.0
cont = 0
cantidad = int (input("Cuanta cantidad de cobros desea ingresar: "))
for x in range(cantidad):
    ahorros = float(input("Ingresa el cobro: "))
    acu = acu + ahorros
    cont = cont + 1
print("La acumulación de los cobros es de: " , acu)
print("Contador de cuantos cobros ingresó: ", cont)
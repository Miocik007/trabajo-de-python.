acu = 0.0
puntos = 0
cont = 0
set = int (input("Cuantos sets se hicieron en total: "))
for x in range(set):
    puntos = int(input("Ingresa los puntos del set: "))
    acu = acu + puntos
    cont = cont + 1
print("La acumulación de puntos es de: " , acu)
print("Contador de cuantos puntos ingresó: ", cont)
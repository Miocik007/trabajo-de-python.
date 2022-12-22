acu = 0.0
goles = 0
cont = 0
for x in range(2):
    goles = int(input("Ingresa los goles del partido: "))
    acu = acu + goles
    cont = cont + 1
print("La acumulación de goles es de: " , acu)
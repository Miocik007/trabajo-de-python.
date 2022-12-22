acu = 0.0
alumnos = 0.0
cont = 0
cantidad = int (input("Ingresa la cantidad de alumnos: "))
for x in range(cantidad):
    alumnos = float(input("Ingresa la nota del alumno: "))
    acu = acu + alumnos
    cont = cont + 1
print("La acumulación de la nota de los alumnos es de: " , acu)
print("Contador de cuantos alumnos ingresó: ", cont)
print("---") 
print("EjercicioN: VERIFICAR SI EL AÑO ES BISIESTO.") 
print("---")
año = int( input("Ingrese año: "))
print("\nSALIDA: ")
print("---") 
if (año % 400 == 0) or (año % 4 == 0) and (año % 100 != 0): print("El año es BISIESTO")
else : print("El año no es BISIESTO")
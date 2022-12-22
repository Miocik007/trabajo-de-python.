suma = 0.0
ropa = 0.0
pago = 0.0
for x in range(3):
    ropa = float(input("Ingresa el precio de la prenda: "))
    suma = suma + ropa
if suma > 170:
 print ("Se lleva su descuento")
 descuento = 10/100 * suma
 print ("el descuento es de: ", descuento)
elif 170 >= suma:
 print ("No te llevas ningun descuento")
pago = suma - descuento
print("La suma de las prendas es de: " , suma)
print("El pago sería de: ",pago)
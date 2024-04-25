vendedor = input("ingrese el nombre del vendedor: ")
sueldo = float(input("ingrese el sueldo :" ))
venta1 = float(input("ingrese la venta 1: "))
venta2 = float(input("ingrese la venta 2: "))
venta3 = float(input("ingrese la venta 3: "))
#
comision = (venta1+venta2+venta3)  * .10 #
print("el nombre del vendedor es ;", vendedor)
print("el sueldo del vendedor es :", sueldo)
print("la comision del mes por las tres ventas es : ",comision)
print("el sueldo total con la comision es: ",sueldo+comision)
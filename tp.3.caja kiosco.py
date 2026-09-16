# EJERCICIO 1 - CAJA DEL KIOSCO

# Nombre del cliente
nombre = input("Cliente: ")

while nombre == "" or not nombre.isalpha():
    print("Error: ingrese un nombre válido.")
    nombre = input("Cliente: ")


# Cantidad de productos
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: la cantidad debe ser un número entero mayor que 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)


# Totales
total_sin_descuentos = 0
total_con_descuentos = 0


# Productos
for i in range(cantidad):

    precio = input(f"Producto {i + 1} - Precio: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {i + 1} - Precio: ")

    precio = int(precio)

    # Acumular precio original
    total_sin_descuentos += precio

    # Descuento
    descuento = input("Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()

    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    # Acumular precio con descuento
    total_con_descuentos += precio_final


# Cálculos finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad


# Mostrar resultados
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")





inventario = 100
print(f"el inventario contiene {inventario} hamburguesas")
while inventario > 0:
    if inventario <= 100:
        print("Advertencia: el inventario esta casi vacio.")
    num_hamburguesas = int(input("¿cuantas hamburguesas quiere el cliente?"))
    if num_hamburguesas > inventario:
        print (f"no hay suficientes hamburguesas en stock. Solo hay {inventario},hamburguesas disponibles.")
    else:
        inventario -= num_hamburguesas
        print (f"el cliente ha pedido {num_hamburguesas} hamburguesas. el inventario ahora tiene {inventario} hamburguess.")

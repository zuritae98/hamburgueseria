invetario = 200
ventas = 0
print (f"En el stock quedan {invetario}")
while invetario > 0:
    if invetario <= 20:
        print("Alerta pocos calzados en el stock")
    num_zapatos = (int(input("¿cuantos zapatos desea llevar el cliente?")))
    if num_zapatos > invetario:
        print("No hay suficientes zapatos en la tienda. solo queda",invetario, "zapatos disponibles")
    else:
        invetario -=num_zapatos
        print(f"el cliente ha pedido {num_zapatos} zapatos. En el stock queda {invetario} zapatos")
        ventas +=1
        print(f"se han hecho {ventas} ventas")
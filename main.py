import productos
import pedidos
import historial
import webbrowser

while True:
    print("\n--- TIENDA ---")
    print("1. Ver productos")
    print("2. Agregar producto al pedido")
    print("3. Ver pedido")
    print("4. Ver historial")
    print("5. Salir")
    print("6. Ver repositorio en GitHub") 

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        productos.mostrar_productos()

    elif opcion == "2":
        productos.mostrar_productos()
        try:
            index = int(input("Seleccione el número del producto: ")) - 1
            cantidad = int(input("Cantidad: "))

            producto = productos.productos[index]
            pedidos.agregar_producto(producto, cantidad)

        except:
            print("Error, ingrese valores válidos")

    elif opcion == "3":
        total = pedidos.mostrar_pedido()
        historial.guardar_historial(pedidos.pedido)

    elif opcion == "4":
        historial.ver_historial()

    elif opcion == "5":
        print("Gracias por usar la tienda")
        break
    
    
    elif opcion == "6":
     print("Abriendo repositorio en GitHub...")
     webbrowser.open("https://github.com/Proyecto18-00/tienda-py.git")

else:
    print("Opción inválida") 
def guardar_historial(pedido):
    with open("historial.txt", "a") as archivo:
        for item in pedido:
            archivo.write(f"{item['nombre']} - Cantidad: {item['cantidad']} - Total: {item['total']}\n")
        archivo.write("-----\n")

def ver_historial():
    print("\n--- HISTORIAL DE COMPRAS ---")
    with open("historial.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido) 
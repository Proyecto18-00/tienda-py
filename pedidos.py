pedido = []

def agregar_producto(producto, cantidad):
    total = producto["precio"] * cantidad

    pedido.append({
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio": producto["precio"],
        "total": total
    })

    print("Producto agregado al pedido")

def mostrar_pedido():
    print("\n--- PEDIDO ---")
    total_general = 0

    for item in pedido:
        print(f"{item['nombre']} x{item['cantidad']} - ${item['total']}")
        total_general += item["total"]

    print("Total a pagar:", total_general)
    return total_general
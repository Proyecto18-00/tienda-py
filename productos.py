productos = [
    {"nombre": "Arroz", "precio": 2000},
    {"nombre": "Leche", "precio": 3000},
    {"nombre": "Pan", "precio": 1500},
    {"nombre": "Huevos", "precio": 500}
]

def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto['nombre']} - ${producto['precio']}")
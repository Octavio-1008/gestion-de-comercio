# --- Datos en memoria (seed inicial) ---
productos = [
    {"sku": "PROT-001", "nombre": "Whey Protein", "sabor": "Vainilla", "categoria": "Proteínas", "precio": 29999.0, "stock": 20},
    {"sku": "PROT-002", "nombre": "Whey Protein", "sabor": "Chocolate", "categoria": "Proteínas", "precio": 29999.0, "stock": 15},
    {"sku": "CREA-101", "nombre": "Creatina Monohidratada", "sabor": "Neutro", "categoria": "Creatinas", "precio": 19999.0, "stock": 30},
]

# --- Funciones básicas ---
def listaDeProductos():
    if not productos:
        print("\nNo hay productos cargados.")
        return
    print("\n--- Lista de productos ---")
    for p in productos:
        print(f"SKU: {p['sku']} | {p['nombre']} ({p['sabor']}) | Cat: {p['categoria']} | $ {p['precio']:.2f} | Stock: {p['stock']}")

# --- Menú principal ---
def main():
    while True:
        print("\n" + "="*60)
        print("EMINENCIA - SISTEMA DE GESTIÓN (CONSOLA)".center(60))
        print("="*60)
        print("1) Listar productos")
        print("0) Salir")
        opcionElegida = input("> Opción: ").strip()
        if opcionElegida == "1":
            listaDeProductos()
        elif opcionElegida == "0":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

main()


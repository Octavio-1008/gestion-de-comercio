# Lista de productos sugeridos con ayuda de IA para la creatividad y variedad de los mismos
productos = [
    {"sku":"PROT-001","nombre":"Whey Protein","sabor":"Vainilla","categoria":"Proteínas","precio":29999.0,"stock":20},
    {"sku":"PROT-002","nombre":"Whey Protein","sabor":"Chocolate","categoria":"Proteínas","precio":29999.0,"stock":15},
    {"sku":"PROT-003","nombre":"Whey Protein","sabor":"Frutilla","categoria":"Proteínas","precio":29999.0,"stock":18},
    {"sku":"PROT-004","nombre":"Whey Protein","sabor":"Cookies & Cream","categoria":"Proteínas","precio":30999.0,"stock":12},
    {"sku":"PROT-005","nombre":"Whey Protein","sabor":"Banana","categoria":"Proteínas","precio":29999.0,"stock":14},
    {"sku":"PROT-006","nombre":"Whey Protein","sabor":"Dulce de Leche","categoria":"Proteínas","precio":31999.0,"stock":10},
    {"sku":"ISOL-010","nombre":"Whey Isolate","sabor":"Vainilla","categoria":"Proteínas","precio":36999.0,"stock":12},
    {"sku":"ISOL-011","nombre":"Whey Isolate","sabor":"Chocolate","categoria":"Proteínas","precio":36999.0,"stock":10},
    {"sku":"ISOL-012","nombre":"Whey Isolate","sabor":"Frutilla","categoria":"Proteínas","precio":36999.0,"stock":9},
    {"sku":"ISOL-013","nombre":"Whey Isolate","sabor":"Cookies & Cream","categoria":"Proteínas","precio":37999.0,"stock":7},
    {"sku":"CASE-030","nombre":"Caseína Micelar","sabor":"Vainilla","categoria":"Proteínas","precio":33999.0,"stock":11},
    {"sku":"CASE-031","nombre":"Caseína Micelar","sabor":"Chocolate","categoria":"Proteínas","precio":33999.0,"stock":10},
    {"sku":"CASE-032","nombre":"Caseína Micelar","sabor":"Frutilla","categoria":"Proteínas","precio":33999.0,"stock":9},
    {"sku":"CASE-033","nombre":"Caseína Micelar","sabor":"Cookies & Cream","categoria":"Proteínas","precio":34999.0,"stock":6},
    {"sku":"VEGP-020","nombre":"Proteína Vegana (Arveja/Arroz)","sabor":"Chocolate","categoria":"Proteínas","precio":33999.0,"stock":9},
    {"sku":"VEGP-021","nombre":"Proteína Vegana (Arveja/Arroz)","sabor":"Vainilla","categoria":"Proteínas","precio":33999.0,"stock":11},
    {"sku":"VEGP-022","nombre":"Proteína Vegana (Arveja/Arroz)","sabor":"Frutilla","categoria":"Proteínas","precio":33999.0,"stock":8},
    {"sku":"GAIN-700","nombre":"Ganador de Peso","sabor":"Vainilla","categoria":"Ganadores","precio":31999.0,"stock":8},
    {"sku":"GAIN-701","nombre":"Ganador de Peso","sabor":"Chocolate","categoria":"Ganadores","precio":31999.0,"stock":7},
    {"sku":"GAIN-702","nombre":"Ganador de Peso","sabor":"Banana","categoria":"Ganadores","precio":31999.0,"stock":6},
    {"sku":"GAIN-703","nombre":"Ganador de Peso","sabor":"Cookies & Cream","categoria":"Ganadores","precio":32999.0,"stock":5},
    {"sku":"CREA-101","nombre":"Creatina Monohidratada","sabor":"Neutro","categoria":"Creatinas","precio":19999.0,"stock":30},
    {"sku":"CREA-102","nombre":"Creatina Micronizada","sabor":"Neutro","categoria":"Creatinas","precio":20999.0,"stock":22},
    {"sku":"CREA-103","nombre":"Creatina Creapure","sabor":"Neutro","categoria":"Creatinas","precio":24999.0,"stock":16},
    {"sku":"CREA-104","nombre":"Creatina + Betaína","sabor":"Neutro","categoria":"Creatinas","precio":22999.0,"stock":12},
    {"sku":"CREA-105","nombre":"Creatina en Cápsulas","sabor":"Neutro","categoria":"Creatinas","precio":21999.0,"stock":18},
    {"sku":"AMIN-210","nombre":"BCAA 2:1:1","sabor":"Frutilla","categoria":"Aminoácidos","precio":14999.0,"stock":25},
    {"sku":"AMIN-211","nombre":"BCAA 2:1:1","sabor":"Naranja","categoria":"Aminoácidos","precio":14999.0,"stock":20},
    {"sku":"AMIN-212","nombre":"EAA (Aminoácidos Esenciales)","sabor":"Tropical","categoria":"Aminoácidos","precio":17999.0,"stock":14},
    {"sku":"AMIN-213","nombre":"EAA (Aminoácidos Esenciales)","sabor":"Uva","categoria":"Aminoácidos","precio":17999.0,"stock":12},
    {"sku":"AMIN-214","nombre":"BCAA 4:1:1","sabor":"Lima Limón","categoria":"Aminoácidos","precio":15999.0,"stock":17},
    {"sku":"GLUT-300","nombre":"Glutamina","sabor":"Neutro","categoria":"Aminoácidos","precio":13999.0,"stock":26},
    {"sku":"GLUT-301","nombre":"Glutamina","sabor":"Frutilla","categoria":"Aminoácidos","precio":13999.0,"stock":12},
    {"sku":"GLUT-302","nombre":"Glutamina + Zinc","sabor":"Neutro","categoria":"Aminoácidos","precio":14999.0,"stock":11},
    {"sku":"PRET-400","nombre":"Pre-entreno","sabor":"Cítrico","categoria":"Pre-entrenos","precio":16999.0,"stock":19},
    {"sku":"PRET-401","nombre":"Pre-entreno","sabor":"Blueberry","categoria":"Pre-entrenos","precio":16999.0,"stock":13},
    {"sku":"PRET-402","nombre":"Pre-entreno","sabor":"Sandía","categoria":"Pre-entrenos","precio":16999.0,"stock":15},
    {"sku":"PRET-403","nombre":"Pre-entreno","sabor":"Mango Maracuyá","categoria":"Pre-entrenos","precio":16999.0,"stock":12},
    {"sku":"PRET-404","nombre":"Pre-entreno Sin Cafeína","sabor":"Cítrico","categoria":"Pre-entrenos","precio":15999.0,"stock":10},
    {"sku":"PRET-405","nombre":"Pre-entreno + Nitratos","sabor":"Lima Limón","categoria":"Pre-entrenos","precio":18999.0,"stock":9},
    {"sku":"VITA-500","nombre":"Multivitamínico","sabor":"Neutro","categoria":"Vitaminas","precio":8999.0,"stock":40},
    {"sku":"VITA-501","nombre":"Multivitamínico Mujer","sabor":"Neutro","categoria":"Vitaminas","precio":9499.0,"stock":18},
    {"sku":"VITA-502","nombre":"Vitamina D3 5000UI","sabor":"Neutro","categoria":"Vitaminas","precio":6999.0,"stock":22},
    {"sku":"VITA-503","nombre":"Magnesio Citrato","sabor":"Neutro","categoria":"Vitaminas","precio":7499.0,"stock":24},
    {"sku":"VITA-504","nombre":"Vitamina C 1000mg","sabor":"Neutro","categoria":"Vitaminas","precio":6499.0,"stock":28},
    {"sku":"VITA-505","nombre":"Complejo B","sabor":"Neutro","categoria":"Vitaminas","precio":7999.0,"stock":21},
    {"sku":"VITA-506","nombre":"Zinc 25mg","sabor":"Neutro","categoria":"Vitaminas","precio":6299.0,"stock":26},
    {"sku":"VITA-507","nombre":"Hierro","sabor":"Neutro","categoria":"Vitaminas","precio":6199.0,"stock":17},
    {"sku":"VITA-508","nombre":"Calcio + Vitamina D","sabor":"Neutro","categoria":"Vitaminas","precio":8299.0,"stock":19},
    {"sku":"VITA-509","nombre":"Potasio","sabor":"Neutro","categoria":"Vitaminas","precio":7099.0,"stock":15},
    {"sku":"VITA-510","nombre":"Vitamina K2 + D3","sabor":"Neutro","categoria":"Vitaminas","precio":9999.0,"stock":12},
    {"sku":"OMEG-600","nombre":"Omega-3 1000mg","sabor":"Neutro","categoria":"Omega","precio":10999.0,"stock":28},
    {"sku":"OMEG-601","nombre":"Omega-3 2000mg","sabor":"Neutro","categoria":"Omega","precio":13999.0,"stock":14},
    {"sku":"OMEG-602","nombre":"Aceite de Krill","sabor":"Neutro","categoria":"Omega","precio":17999.0,"stock":9},
    {"sku":"TERM-330","nombre":"Termogénico","sabor":"Neutro","categoria":"Quemadores","precio":16999.0,"stock":12},
    {"sku":"TERM-331","nombre":"L-Carnitina Líquida","sabor":"Frutilla","categoria":"Quemadores","precio":12999.0,"stock":17},
    {"sku":"TERM-332","nombre":"L-Carnitina Cápsulas","sabor":"Neutro","categoria":"Quemadores","precio":11999.0,"stock":21},
    {"sku":"TERM-333","nombre":"Extracto de Té Verde","sabor":"Neutro","categoria":"Quemadores","precio":9999.0,"stock":16},
    {"sku":"TERM-334","nombre":"CLA (Ácido Linoleico Conjugado)","sabor":"Neutro","categoria":"Quemadores","precio":10999.0,"stock":14},
    {"sku":"HYDR-800","nombre":"Electrolitos","sabor":"Limón","categoria":"Hidratación","precio":7999.0,"stock":20},
    {"sku":"HYDR-801","nombre":"Electrolitos","sabor":"Naranja","categoria":"Hidratación","precio":7999.0,"stock":19},
    {"sku":"HYDR-802","nombre":"Electrolitos","sabor":"Frutilla","categoria":"Hidratación","precio":7999.0,"stock":17},
    {"sku":"HYDR-803","nombre":"Bebida Isotónica","sabor":"Uva","categoria":"Hidratación","precio":5999.0,"stock":22},
    {"sku":"HYDR-804","nombre":"Bebida Isotónica","sabor":"Tropical","categoria":"Hidratación","precio":5999.0,"stock":20},
    {"sku":"HYDR-805","nombre":"Gel Energético","sabor":"Limón","categoria":"Hidratación","precio":3499.0,"stock":25},
    {"sku":"HYDR-806","nombre":"Gel Energético","sabor":"Frutilla","categoria":"Hidratación","precio":3499.0,"stock":23},
    {"sku":"CARB-840","nombre":"Maltodextrina","sabor":"Neutro","categoria":"Carbohidratos","precio":10999.0,"stock":18},
    {"sku":"CARB-841","nombre":"Dextrosa","sabor":"Neutro","categoria":"Carbohidratos","precio":9999.0,"stock":16},
    {"sku":"CARB-842","nombre":"Ciclodextrina","sabor":"Neutro","categoria":"Carbohidratos","precio":18999.0,"stock":10},
    {"sku":"CARB-843","nombre":"Palatinosa (Isomaltulosa)","sabor":"Neutro","categoria":"Carbohidratos","precio":16999.0,"stock":9},
    {"sku":"SNCK-900","nombre":"Barrita Proteica","sabor":"Chocolate","categoria":"Snacks","precio":2499.0,"stock":60},
    {"sku":"SNCK-901","nombre":"Barrita Proteica","sabor":"Maní","categoria":"Snacks","precio":2499.0,"stock":55},
    {"sku":"SNCK-902","nombre":"Cookie Proteica","sabor":"Chips de chocolate","categoria":"Snacks","precio":2999.0,"stock":35},
    {"sku":"SNCK-903","nombre":"Brownie Proteico","sabor":"Chocolate","categoria":"Snacks","precio":3499.0,"stock":28},
    {"sku":"SNCK-904","nombre":"Chips Proteicos","sabor":"Salados","categoria":"Snacks","precio":3299.0,"stock":25},
    {"sku":"SNCK-905","nombre":"Mantequilla de Maní","sabor":"Clásica","categoria":"Snacks","precio":5499.0,"stock":30},
    {"sku":"SNCK-906","nombre":"Mantequilla de Maní","sabor":"Crunchy","categoria":"Snacks","precio":5699.0,"stock":26},
    {"sku":"SNCK-907","nombre":"Syrup Cero","sabor":"Chocolate","categoria":"Snacks","precio":3999.0,"stock":22},
    {"sku":"SNCK-908","nombre":"Syrup Cero","sabor":"Maple","categoria":"Snacks","precio":3999.0,"stock":20},
    {"sku":"SNCK-909","nombre":"Tostadas de Arroz","sabor":"Clásicas","categoria":"Snacks","precio":1999.0,"stock":34},
    {"sku":"SNCK-910","nombre":"Avena Instantánea","sabor":"Neutro","categoria":"Snacks","precio":3499.0,"stock":27},
    {"sku":"SNCK-911","nombre":"Mix de Frutos Secos","sabor":"Clásico","categoria":"Snacks","precio":5999.0,"stock":18},
    {"sku":"SNCK-912","nombre":"Pasta de Almendra","sabor":"Clásica","categoria":"Snacks","precio":7999.0,"stock":12},
    {"sku":"COLA-950","nombre":"Colágeno Hidrolizado","sabor":"Neutro","categoria":"Bienestar","precio":14999.0,"stock":18},
    {"sku":"COLA-951","nombre":"Colágeno + Vitamina C","sabor":"Naranja","categoria":"Bienestar","precio":15999.0,"stock":14},
    {"sku":"COLA-952","nombre":"Colágeno Marino","sabor":"Neutro","categoria":"Bienestar","precio":19999.0,"stock":9},
    {"sku":"COLA-953","nombre":"Colágeno + Ácido Hialurónico","sabor":"Frutilla","categoria":"Bienestar","precio":17999.0,"stock":11},
    {"sku":"COLA-954","nombre":"Colágeno Tipo II","sabor":"Neutro","categoria":"Bienestar","precio":18999.0,"stock":10},
    {"sku":"JOIN-960","nombre":"Soporte Articular (Glucosamina)","sabor":"Neutro","categoria":"Bienestar","precio":12999.0,"stock":16},
    {"sku":"JOIN-961","nombre":"Condroitina + MSM","sabor":"Neutro","categoria":"Bienestar","precio":13999.0,"stock":13},
    {"sku":"JOIN-962","nombre":"Cúrcuma + Piperina","sabor":"Neutro","categoria":"Bienestar","precio":11999.0,"stock":15},
    {"sku":"PROB-970","nombre":"Probióticos 20B CFU","sabor":"Neutro","categoria":"Bienestar","precio":13999.0,"stock":10},
    {"sku":"PROB-971","nombre":"Probióticos 50B CFU","sabor":"Neutro","categoria":"Bienestar","precio":17999.0,"stock":8},
    {"sku":"PROB-972","nombre":"Probióticos Kids","sabor":"Vainilla","categoria":"Bienestar","precio":12999.0,"stock":12},
    {"sku":"FIBR-980","nombre":"Fibra Soluble","sabor":"Neutro","categoria":"Bienestar","precio":7999.0,"stock":12},
    {"sku":"FIBR-981","nombre":"Inulina de Achicoria","sabor":"Neutro","categoria":"Bienestar","precio":8499.0,"stock":10},
    {"sku":"FIBR-982","nombre":"Psyllium Husk","sabor":"Neutro","categoria":"Bienestar","precio":8999.0,"stock":9},
    {"sku":"CAFE-990","nombre":"Cafeína Cápsulas 200mg","sabor":"Neutro","categoria":"Pre-entrenos","precio":5999.0,"stock":30},
    {"sku":"CAFE-991","nombre":"Cafeína Tabletas 100mg","sabor":"Neutro","categoria":"Pre-entrenos","precio":4499.0,"stock":26},
    {"sku":"BET-995","nombre":"Beta Alanina","sabor":"Neutro","categoria":"Pre-entrenos","precio":10999.0,"stock":13},
    {"sku":"CITR-996","nombre":"Citrulina Malato","sabor":"Neutro","categoria":"Pre-entrenos","precio":11999.0,"stock":11},
    {"sku":"ARGN-997","nombre":"Arginina AKG","sabor":"Neutro","categoria":"Pre-entrenos","precio":9999.0,"stock":12},
    {"sku":"BEBI-820","nombre":"Batido RTD (Listo para tomar)","sabor":"Vainilla","categoria":"Bebidas","precio":4999.0,"stock":22},
    {"sku":"BEBI-821","nombre":"Batido RTD (Listo para tomar)","sabor":"Chocolate","categoria":"Bebidas","precio":4999.0,"stock":21},
    {"sku":"BEBI-822","nombre":"Batido RTD (Listo para tomar)","sabor":"Frutilla","categoria":"Bebidas","precio":4999.0,"stock":18},
    {"sku":"BEBI-823","nombre":"Agua Proteica","sabor":"Lima Limón","categoria":"Bebidas","precio":4599.0,"stock":19},
    {"sku":"ASHW-720","nombre":"Ashwagandha","sabor":"Neutro","categoria":"Bienestar","precio":11999.0,"stock":14},
    {"sku":"MELA-730","nombre":"Melatonina 3mg","sabor":"Neutro","categoria":"Bienestar","precio":6999.0,"stock":17},
    {"sku":"RHOD-731","nombre":"Rhodiola Rosea","sabor":"Neutro","categoria":"Bienestar","precio":10999.0,"stock":8},
    {"sku":"MACA-740","nombre":"Maca Andina","sabor":"Neutro","categoria":"Bienestar","precio":9999.0,"stock":12},
]

# Variables a usar mas adelante
clientes = []  # ejemplo para tener en cuenta a futuro: {"dni":"", "nombre":"", "telefono":"", "email":""} o similar
ventas = []    # " " {"nro":1, "fecha":"04-09-2025", "cliente_dni":"", "items":[{"sku":"PROT-001","cantidad":2,"precio_unit":29999.0}], "total":59998.0} aprox

# Funciones basicas implementadas
def listaDeProductos():
    if not productos:
        print("\nNo hay productos cargados.")
        return
    print("\n--- Lista de productos ---")
    for elemento in productos:
        print(f"SKU: {elemento['sku']} | {elemento['nombre']} ({elemento['sabor']}) | "
              f"Cat: {elemento['categoria']} | $ {elemento['precio']:.2f} | Stock: {elemento['stock']}")

def buscarProductos():
    print("\n--- Buscar productos (por nombre, sabor, categoría o SKU) ---")
    print('Para volver al menú escriba "0".')
    productoParaBuscar = input("Ingrese el producto que desea buscar: ").strip()

    if productoParaBuscar == "0":
        return
    if productoParaBuscar == "":
        print("Búsqueda vacía. Intente nuevamente desde el menú.")
        return

    productoParaBuscar = productoParaBuscar.lower()
    cantidadEncontrados = 0

    for elemento in productos:
        nombre = elemento["nombre"].lower()
        sabor = elemento["sabor"].lower()
        categoria = elemento["categoria"].lower()
        sku = elemento["sku"].lower()

        if (productoParaBuscar in nombre
            or productoParaBuscar in sabor
            or productoParaBuscar in categoria
            or productoParaBuscar in sku):
            print(f"{elemento['sku']} | {elemento['nombre']} ({elemento['sabor']}) | "
                  f"{elemento['categoria']} | $ {elemento['precio']:.2f} | Stock: {elemento['stock']}")
            cantidadEncontrados += 1

    if cantidadEncontrados == 0:
        print("Producto inválido o no encontrado. Puede buscar por nombre, sabor, categoría o SKU.")

# Funciones a implementar
def altaProducto():
    pass

def editarProducto():
    pass

def eliminarProducto():
    pass

def registrarCliente():
    pass

def listarClientes():
    pass

def buscarCliente():
    pass

def nuevaVenta():
    pass

def listarVentas():
    pass

def reporteStock():
    pass

def reporteVentasDelMes():
    pass

def reporteFacturacionDelMes():
    pass

def productoGanadorDelMes():
    pass

# --- Menú principal ---
def main():
    while True:
        print("\n" + "="*60)
        print("MENÚ DEL SISTEMA DE GESTIÓN DE PRODUCTOS - EMINENCIA".center(60))
        print("="*60)
        print("1) Lista de productos")
        print("2) Buscar productos")
        print("0) Salir")
        opcionElegida = input("> Opción: ").strip()

        if opcionElegida == "1":
            listaDeProductos()
        elif opcionElegida == "2":
            buscarProductos()
        elif opcionElegida == "0":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

main()

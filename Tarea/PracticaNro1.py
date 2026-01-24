# Realiza un menu iterativo
# Cada opcion debe ser una funcion => fz()
# Opcion 1 : Sumar 2 numeros
# Opcion 2 : Crea una coleccion de productos para un mercado
# Opcion 3 : Agrega un nuevo producto a la coleccion
# Opcion 4 : Mostrar el producto de precio mas bajo
# Opcion 5 : Salir

#productos = []

msg = """
    ============= BIENVENIDOS AL SISTEMA ================
    Ingrese una opcion:

    1. Sumar 2 numeros.
    2. Crear una coleccion de productos para un mercado.
    3. Agregar un nuevo producto a la colección.
    4. Mostrar el producto de precio mas bajo.
    5. Salir.
    ====================================================
    """

def sumarDosNumeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")

def crearColeccionProductos():
    productos = []
    n = int(input("¿Cuántos productos desea agregar? "))
    for _ in range(n):
        producto = {}
        producto["nombre"] = input("Ingrese el nombre del producto: ")
        producto["precio"] = float(input("Ingrese el precio del producto: "))
        productos.append(producto)
    print("Colección de productos creada.")
    return productos

def AgregarNuevoProducto(productos):
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto: ")
    producto["precio"] = float(input("Ingrese el precio del producto: "))
    productos.append(producto)
    print("Producto agregado a la colección.")

def MostrarProductoPrecioMasBajo(productos):
    if productos:
        producto_mas_bajo = min(productos, key=lambda x: x["precio"])
        print(
            f"El producto de precio más bajo es: "
            f"{producto_mas_bajo['nombre']} - S/ {producto_mas_bajo['precio']}"
        )
    else:
        print("No hay productos en la colección.")

while True:
    print(msg)
    opcion = int(input("Ingrese una opción: ")) 
    if opcion == 1:
        sumarDosNumeros()
    elif opcion == 2:
        productos = crearColeccionProductos()
    elif opcion == 3:
        AgregarNuevoProducto(productos)
    elif opcion == 4:
        MostrarProductoPrecioMasBajo(productos)
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Ingrese una opción válida.")
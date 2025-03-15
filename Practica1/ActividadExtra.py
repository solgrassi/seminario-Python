# Creacion del inventario
inventario = {}

# Funcionalidades del inventario
# Todos los productos se ponen en minuscula para no manipular un mismo producto como diferente por uso de mayúsculas.

def agregar_producto(): 
    nombre = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("ingrese la cantidad a añadir: "))
    # Si el producto ya existe
    if nombre in inventario:
        inventario[nombre] += cantidad
        input("Producto ya existente, stock actualizado!")
    else:
        inventario[nombre] = cantidad
        input(f"Producto: {nombre}, agregado correctamente!")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
    if nombre in inventario:
        del inventario[nombre]
        print(f"El producto: {nombre} fue eliminado con exito!")
    else:
        print("El producto que intenta eliminar no se encuentra en el inventario.")

def buscar_producto():
    nombre = input("ingrese el nombre del producto a buscar: ").lower()
    if nombre in inventario:
        print(f"El producto se encuentra en el inventario y cuenta con un stock de: {inventario[nombre]}.")
    else: 
        print("El producto no se encuentra en el inventario.")

def actualizar_stock():
    nombre = input("Ingrese el nombre del producto: ").lower()
    if nombre in inventario:
        cant = int(input ("Ingrese el stock actual (se reemplazará el anterior): "))
        inventario[nombre] = cant
        print("Stock actualizado correctamente!")
    else:
        print("El producto no se encuentra en el inventario.")

def mostar_inventario():
    if not inventario:
        print("Inventario vacio.")
    else:
        print("Inventario: ")
        for i in inventario:
            print(f"Producto: {i}, cantidad: {inventario[i]}.")

#diccionario de funcionalidades
funciones = {
    1: agregar_producto,
    2: eliminar_producto,
    3: buscar_producto,
    4: actualizar_stock,
    5: mostar_inventario,
}

# Menu interactivo
sigue = True 
sentence = "Bienvenido/a al menu interactivo"
print(sentence.center(60, " "))
print("1.Agregar un producto al inventario.")
print("2.Eliminar un producto del inventario.")
print("3.Informar stock de un producto.")
print("4.Actualizar el stock de un producto.")
print("5.Mostrar inventario completo.")
print("6.Salir del menu interactivo")
while sigue:
    print()
    eleccion = input("Por favor, seleccione el numero de opcion que quiere realizar: ")
    if eleccion.isnumeric():
        eleccion = int(eleccion)
        if eleccion == 6:
            sigue = False
            break
        elif eleccion in funciones:
            funciones[eleccion]()
        else:
            print("Opcion no valida. Intente nuevamente")
    else:
        print("Opcion no valida. Intente nuevamente")
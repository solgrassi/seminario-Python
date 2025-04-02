def espacio_extra (nombres):
    """
    Recibe una lista de strings y los devuelve sin espacios extra
    """
# Elimina los espcacios extra en los cleintes que no son ni vacio ni none
    clientes = [
        cliente.strip() for cliente in nombres if cliente and cliente.strip()
    ]
    return clientes


def formato_titulo (nombres):
    """
    Recibe una lista de strings y los devuelve en formato titulo: primer letra
    mayuscula, el resto minuscula. 
    """
    clientes = [cliente.title() for cliente in nombres if cliente and cliente.capitalize()]
    return clientes


def eliminar_duplicados (nombres):
    """
    Elimina los datos (str) duplicados a partir de una lista
    """
    # Utiliza un comjunto que no almacena datos repetidos y luego lo convierte
    # en lista
    sin_rep = list(set(nombres))
    return sin_rep


def eliminar_nulo_vacio (nombres):
    """
    Elimina los elementos (str) nulos o vacios de una lista.
    """
# Tiene en cuenta los valores de verdad para guardar los clientes, 
# none o vacio = False.
    clientes = [cliente for cliente in nombres if cliente and cliente.strip()]
    return clientes


def limpiar_todo (clientes):
    """
    Aplica todas las funciones sobre la lista de clientes, e imprime el 
    resultado de la limpieza completa.
    Parametros
    lista de clientes (list)
    Retorno
    lista de clientes actualizada y purificada (list)
    """
    clientes = espacio_extra(clientes)
    clientes = formato_titulo(clientes)
    clientes = eliminar_duplicados(clientes)
    clientes = eliminar_nulo_vacio(clientes)
    clientes.sort()
    return clientes
    


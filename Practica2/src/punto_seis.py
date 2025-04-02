def contar_repeticiones (descripciones):
    """
    Cuenta cuántas veces se mencionan las palabras 'entretenimiento', 'música' 
    y 'charla' en una lista de descripciones.
    Parametros:
    lista tipo String
    Retorno:
    diccionario con la cantidad de repeticiones de cada palabra.
    """
    palabras = ["entretenimiento", "música", "charla"]
    menciones = {}
    for palabra in palabras:
         menciones[palabra] = sum(p.lower().split().count(palabra) for p in descripciones)
    return menciones


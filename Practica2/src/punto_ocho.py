def es_anagrama (uno,dos):
    """
    determina si dos plabras son anagramas o no.
    Parametros:
    palabra uno (str), palabra dos (str)
    Retorno:
    str - si son anagramas o no. 
    """
    anagrama = sorted(uno.lower()) == sorted(dos.lower())
    resul = ((f"las palabras '{uno}' y '{dos}'") + 
            ("son anagramas." if anagrama else "no son anagramas."))
    return resul


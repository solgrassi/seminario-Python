def validar_usuario (user):
    """
    Valida un dato teniendo en cuenta:
    que tenga al menos 5 caracteres, al menos un numero, al menos una letra
    mayuscula, y solo tenga letras y numeros. 
    Parametros: 
    usuario: string
    retorno:
    str - si es válido o no
    """

    if (len(user)< 5):
        return ("El nombre de usuario no cumple con los requisitos.")
    if not(any(dig.isnumeric() for dig in user)):
        return ("El nombre de usuario no cumple con los requisitos.")
    if not(any( dig.isupper() for dig in user)):
        return ("El nombre de usuario no cumple con los requisitos.")
    if not(user.isalnum()):
        return ("El nombre de usuario no cumple con los requisitos.")
    return ("El usuario ingresado es válido.")     


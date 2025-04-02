def clasificar_reaccion(tiempo):
    """
    Indica a que categoria pertenece el usuario dependiendo los ms ingresados.
    Parametros:
    ms de reaccion (int)
    Retorno
    str - categoria a la que pertenece. 
    """
    if (tiempo<200):
        return "Categoria: Rapido"
    if (tiempo>=200) and (tiempo<=500):
        return "Categoria: Normal"
    if (tiempo>500):
        return "Categoria: Lento"
    tie = int(input("ingrese su tiempo en ms"))
    print(clasificar_reaccion(tie))

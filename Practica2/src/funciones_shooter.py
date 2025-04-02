def  calcular_puntos(kills,assist,death):
    """
    Calcula el puntaje de un jugador basado en kills, asistencias y muertes.
    """
    return ((kills * 3 + assist *2) + (-1 if death else 0))







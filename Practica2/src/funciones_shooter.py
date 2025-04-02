def  calcular_puntos(kills,assist,death):
    """
    Calcula el puntaje de un jugador basado en kills, asistencias y muertes.
    """
    return ((kills * 3 + assist *2) + (-1 if death else 0))


def procesar_ronda (infoJugadores, infoGlobal):
    """
    Procesa una ronda para determinar las estadisticas y MVP. 
    Devuelve una tupla con los jugadores y sus datos correspondientes.
    """
    jugadores = []
    for nombre, datos in infoJugadores:
        jugador = {
            'Jugador': nombre,
            'Kills': datos['kills'],
            'Asistencias' : datos['assists'],
            'Muertes' : datos['deaths'],
            'Puntos' : calcular_puntos(datos['kills'], datos['assists'], datos['deaths']),
            'MVPs' : 0
        }
    #agrego a la lista el jugador procesado
    jugadores.append(jugador)
    #Ordeno la lista segun los puntos totales, en orden descendiente(reverse)
    jugadores.sort(key = lambda x: x['points'], reverse=True)
    # El primer jugador sera el MVP
    jugadores[0]['MVPs'] += 1

    for jugador in jugadores:
        if jugador['name'] not in infoGlobal:
            infoGlobal[jugador['name']] = {
                'kills': jugador['kills'],
                'assists': jugador['assists'],
                'deaths': jugador['deaths'],
                'points': jugador['points'],
                'mvps': jugador['mvps']
            }
        else:
            # Apunto a un jugador para actualizar los datos
            estadisticas = infoGlobal[jugador['name']]
            estadisticas['kills'] += jugador['kills']
            estadisticas['assists'] += jugador['assists']
            estadisticas['deaths'] += jugador['deaths']
            estadisticas['points'] += jugador['points']
            estadisticas['mvps'] += jugador['mvps']
    return infoGlobal




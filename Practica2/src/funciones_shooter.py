def  calcular_puntos(kills,assist,death):
    """
    Calcula el puntaje de un jugador basado en kills, asistencias y muertes.
    Parametros:
    kills - int: numero de kills
    assist - int: numero de asistencias
    death - int: si murio o no
    Retorno:
    puntos (int) totales.
    """
    return ((kills * 3 + assist * 1) - (1 if death else 0))


def procesar_ronda (info_jugadores, info_global):
    """
    Procesa una ronda para determinar las estadisticas y MVP. 
    Parametros:
    info_jugadores - dic: una ronda del juego con todos los jugadores.
    info_global- dic: valores acumulados durante las rondas.
    Retorno:
    Devuelve ek nombre del mvp de la ronda
    """
    jugadores = []
    for nombre, datos in info_jugadores.items(): 
        jugador = {
            'name': nombre,
            'kills': datos['kills'],
            'assists' : datos['assists'],
            'deaths' : datos['deaths'],
            'points' : calcular_puntos(
                datos['kills'], datos['assists'], datos['deaths']
            ),
            'mvps' : 0 
        }
        #agrego a la lista el jugador procesado
        jugadores.append(jugador)
    #Ordeno la lista segun los puntos totales, en orden descendiente(reverse)
    jugadores.sort(key = lambda x: x['points'], reverse=True)
    # El primer jugador sera el MVP
    jugadores[0]['mvps'] += 1
    mvp_ronda = jugadores[0]['name']
    
    for jugador in jugadores:
        if jugador['name'] not in info_global:
            info_global[jugador['name']] = {
                'kills': jugador['kills'],
                'assists': jugador['assists'],
                'deaths': jugador['deaths'],
                'points': jugador['points'],
                'mvps': jugador['mvps']
            }
        else:
            # Apunto a un jugador para actualizar los datos
            estadisticas = info_global[jugador['name']]
            estadisticas['kills'] += jugador['kills']
            estadisticas['assists'] += jugador['assists']
            estadisticas['deaths'] += jugador['deaths']
            estadisticas['points'] += jugador['points']
            estadisticas['mvps'] += jugador['mvps']
    return mvp_ronda


def imprimir_ronda (info_global,num,mvp_ronda):
    """
    Imprime cada ronda con todos los jugadores y los valores correspondientes
    en una tabla.
    Parametros:
    info_global -dic: estadisticas acumuladas de las rondas procesadas.
    mvp_ronda - string: nombre del mvp de la ronda.
    num - int : numero de ronda
    Retorno:
    none
    """
    print(f"Ronda numero {num}: ")
    #Imprimir el nombre de la columna alineado a la izquiera y ocupa tantos
    #espacios como este indicado. 
    print(
        f"{'Jugador':<10} {'Kills':<8} {'Asistencias':<12} {'Muertes':<8}"
        f"{'MVPs':<5} {'Puntos':<6}" 
    )
    print("-" * 56)
    # Ordenar los jugadores en orden decreciente por puntos totales.
    jugadoresOrdenados = sorted(
        info_global.items(), key=lambda x: x[1]['points'], reverse=True
    )
    #Imprimir tabla iterando sobre cada jugador
    for nombre, datos in jugadoresOrdenados:
        print(
            f"{nombre:<10} {datos['kills']:<8} {datos['assists']:<12}"
            f"{datos['deaths']:<8} {datos['mvps']:<5} {datos['points']:<6}"
        )
    print ()
    print (f"El MVP de la ronda es: {mvp_ronda}")
    print("-" * 56)
    print()

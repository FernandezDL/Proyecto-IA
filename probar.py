def verificar_condicion_victoria(victorias):
    """Verifica si alguna condición de victoria del juego se ha cumplido."""
    for jugador, elementos in victorias.items():
        # verificar 3 colores distintos en un elemento
        for elemento, colores in elementos.items():
            if len(set(colores))>= 3:
                victoria = {"Elemento": elemento,
                            "Colores" : set(colores)}
                return jugador, victoria
        
        # verificar victoria en 3 elementos con colores distintos
        colores_fuego = elementos['Fuego']
        colores_agua = elementos['Agua']
        colores_nieve = elementos['Nieve']
        victoria = {"Fuego": None, "Agua": None, "Nieve": None}
        for colorF in colores_fuego:
            victoria['Fuego'] = colorF
            for colorA in colores_agua:
                victoria['Agua'] = colorA
                for colorN in colores_nieve:
                    victoria['Nieve'] = colorN
                    colors = [victoria['Fuego'],victoria['Agua'],victoria['Nieve']]
                    if len(set(colors)) == 3:
                        return jugador, victoria
                        
    return None, None


victorias = {"User": {"Fuego": [], "Agua": ['Rojo', 'Naranja','Verde'], "Nieve": []}, 
             "IA": {"Fuego": ['Azul', 'Lila'], "Agua": ['Azul', 'Amarillo'], "Nieve": ['Verde']}}

ganador, victoria = verificar_condicion_victoria(victorias)

print(ganador)
print(victoria)
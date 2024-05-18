from metricas import actualizar_resultados, graficar_resultados, mostrar_porcentaje
from asignarCartas import cargar_cartas, asignar_cartas
from Qlearning import *
import numpy as np
import random

def seleccionar_cartas_mano(mazo):
    """Selecciona 5 cartas aleatorias para la mano inicial y las elimina del mazo."""
    mano = random.sample(mazo, 5)
    for carta in mano:
        mazo.remove(carta)
    return mano, mazo

def mostrar_cartas(mano):
    """Muestra las cartas en la mano del jugador 'user' numeradas."""
    for idx, carta in enumerate(mano, 1):
        print(f"{idx}. {carta}")

def determinar_ganador(carta_user, carta_ia, victorias):
    """Determina el ganador del turno y actualiza el registro de victorias."""
    resultado = ""
    domina = {'Fuego': 'Nieve', 'Nieve': 'Agua', 'Agua': 'Fuego'}
    if domina[carta_user.elemento] == carta_ia.elemento:
        resultado = "User"
    elif domina[carta_ia.elemento] == carta_user.elemento:
        resultado = "IA"
    elif carta_user.elemento == carta_ia.elemento:
        if carta_user.numero > carta_ia.numero:
            resultado = "User"
        elif carta_user.numero < carta_ia.numero:
            resultado = "IA"
        else:
            resultado = "Empate"

    if resultado != "Empate":
        victorias[resultado][carta_user.elemento if resultado == "User" else carta_ia.elemento].append(
            carta_user.color if resultado == "User" else carta_ia.color)

    return resultado

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


def mostrar_victorias(victorias):
    """Muestra el registro actual de victorias."""
    for jugador, elementos in victorias.items():
        print(f"Victorias de {jugador}:")
        for elemento, colores in elementos.items():
            print(f"  {elemento.capitalize()}: {colores}")

def entrenar_ia(episodios=1000):
    inicializar_Q()
    for episodio in range(episodios):
        cartas = cargar_cartas()
        cartas_user, cartas_ia = asignar_cartas(cartas)
        mano_user, mazo_user = seleccionar_cartas_mano(cartas_user)
        mano_ia, mazo_ia = seleccionar_cartas_mano(cartas_ia)
        
        victorias = {"User": {"Fuego": [], "Agua": [], "Nieve": []}, "IA": {"Fuego": [], "Agua": [], "Nieve": []}}
        historial_acciones = []
        turno = 0

        while True:
            turno += 1
            eleccion_user = random.randint(0, len(mano_user) - 1)  # Selección aleatoria del usuario
            carta_user = mano_user.pop(eleccion_user)
            historial_acciones.append(('User', carta_user.elemento, carta_user.numero))

            estado_actual = get_state(victorias, mano_ia, mazo_user, mazo_ia, tuple(historial_acciones))
            eleccion_ia = select_action(estado_actual, mano_ia)
            carta_ia = mano_ia.pop(mano_ia.index(eleccion_ia))
            historial_acciones.append(('IA', carta_ia.elemento, carta_ia.numero))
            
            resultado = determinar_ganador(carta_user, carta_ia, victorias)
            if resultado == "Empate":
                recompensa = reward(False, False)
            else:
                recompensa = reward(resultado == "User", resultado == "IA")

            estado_siguiente = get_state(victorias, mano_ia, mazo_user, mazo_ia, tuple(historial_acciones))
            update_Q(estado_actual, eleccion_ia, recompensa, estado_siguiente, mano_ia)

            ganador, victoria = verificar_condicion_victoria(victorias)
            if ganador:
                actualizar_resultados(ganador)  # Registrar la victoria del juego
                mostrar_porcentaje()
                break

            if mazo_user and mazo_ia:
                nueva_carta_user = random.choice(mazo_user)
                mazo_user.remove(nueva_carta_user)
                mano_user.append(nueva_carta_user)

                nueva_carta_ia = random.choice(mazo_ia)
                mazo_ia.remove(nueva_carta_ia)
                mano_ia.append(nueva_carta_ia)
        
        if episodio % 100 == 0:
            print(f"Episodio {episodio} completado")
    graficar_resultados()

def main():
    entrenar_ia(episodios=10000)
    inicializar_Q()
    cartas = cargar_cartas()
    cartas_user, cartas_ia = asignar_cartas(cartas)
    mano_user, mazo_user = seleccionar_cartas_mano(cartas_user)
    mano_ia, mazo_ia = seleccionar_cartas_mano(cartas_ia)
    
    victorias = {"User": {"Fuego": [], "Agua": [], "Nieve": []}, "IA": {"Fuego": [], "Agua": [], "Nieve": []}}
    historial_acciones = []
    turno = 0

    while True:
        turno += 1
        print(f"\nTurno {turno}")
        print("Mano IA")
        mostrar_cartas(mano_ia)
        print("\n")
        mostrar_cartas(mano_user)
        eleccion_user = int(input("Elige una carta (1-5): ")) - 1
        carta_user = mano_user.pop(eleccion_user)
        historial_acciones.append(('User', carta_user.elemento, carta_user.numero))


        estado_actual = get_state(victorias, mano_ia, mazo_user, mazo_ia, tuple(historial_acciones))
        eleccion_ia = select_action(estado_actual, mano_ia)
        carta_ia = mano_ia.pop(mano_ia.index(eleccion_ia))
        historial_acciones.append(('IA', carta_ia.elemento, carta_ia.numero))
        
        print(f"\nUsuario: {carta_user}")
        print(f"IA: {carta_ia}")

        resultado = determinar_ganador(carta_user, carta_ia, victorias)
        if resultado == "Empate":
            print(resultado)
            recompensa = reward(False, False)
        else:
            print(f"Victoria para: {resultado}")
            recompensa = reward(resultado == "User", resultado == "IA")
                
        estado_siguiente = get_state(victorias, mano_ia, mazo_user, mazo_ia, tuple(historial_acciones))
        update_Q(estado_actual, eleccion_ia, recompensa, estado_siguiente, mano_ia)

        mostrar_victorias(victorias)         
        
        ganador, victoria = verificar_condicion_victoria(victorias)
        if ganador:
            actualizar_resultados(ganador)  # Actualizar el registro de victorias
            #mostrar_porcentaje()
            print(f"\n{ganador} ha ganado el juego!")
            print(victoria)
            guardar_q_table()
            break

        if mazo_user and mazo_ia:
            nueva_carta_user = random.choice(mazo_user)
            mazo_user.remove(nueva_carta_user)
            mano_user.append(nueva_carta_user)

            nueva_carta_ia = random.choice(mazo_ia)
            mazo_ia.remove(nueva_carta_ia)
            mano_ia.append(nueva_carta_ia)

if __name__ == "__main__":
    main()

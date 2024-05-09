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
    print("\nCartas del Usuario:")
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
        # Verificar victoria por tres colores únicos en total, distribuidos en diferentes elementos
        if len(elementos['Fuego']) > 0 and len(elementos['Agua']) > 0 and len(elementos['Nieve']) > 0:
            # Extraer un conjunto de colores por cada elemento
            colores_fuego = set(elementos['Fuego'])
            colores_agua = set(elementos['Agua'])
            colores_nieve = set(elementos['Nieve'])
            
            # Combinar los conjuntos para contar los colores únicos
            colores_unicos = colores_fuego.union(colores_agua).union(colores_nieve)
            
            # Verificar si hay exactamente tres colores diferentes y cada elemento tiene al menos uno
            if len(colores_unicos) == 3 and all(len(colores) == 1 for colores in [colores_fuego, colores_agua, colores_nieve]):
                return jugador
        # Verificar victoria por tres colores únicos en un solo elemento
        for elemento, colores in elementos.items():
            if len(set(colores)) >= 3:
                return jugador
    return None


def mostrar_victorias(victorias):
    """Muestra el registro actual de victorias."""
    for jugador, elementos in victorias.items():
        print(f"Victorias de {jugador}:")
        for elemento, colores in elementos.items():
            print(f"  {elemento.capitalize()}: {colores}")

def main():
    cartas = cargar_cartas()
    cartas_user, cartas_ia = asignar_cartas(cartas)
    mano_user, mazo_user = seleccionar_cartas_mano(cartas_user)
    mano_ia, mazo_ia = seleccionar_cartas_mano(cartas_ia)

    victorias = {"User": {"Fuego": [], "Agua": [], "Nieve": []}, "IA": {"Fuego": [], "Agua": [], "Nieve": []}}
    turno = 0

    while True:
        turno += 1
        print(f"\nTurno {turno}")
        mostrar_cartas(mano_user)
        eleccion_user = int(input("Elige una carta (1-5): ")) - 1
        carta_user = mano_user.pop(eleccion_user)

        # eleccion_ia = random.randint(0, 4)
        # carta_ia = mano_ia.pop(eleccion_ia)
        # Seleccionar acción (carta) para la IA usando Q-learning
        estado_actual = get_state(victorias, mano_ia)
        eleccion_ia = select_action(estado_actual, mano_ia)
        carta_ia = mano_ia.pop(mano_ia.index(eleccion_ia))
        
        print(f"\nUsuario: {carta_user}")
        print(f"IA: {carta_ia}")

        resultado = determinar_ganador(carta_user, carta_ia, victorias)
        if resultado == "Empate":
            print(resultado)
        else:
            print(f"Victoria para: {resultado}")

        mostrar_victorias(victorias)
        
        # Actualizar Q-table
        nuevo_estado = get_state(victorias, mano_ia)
        recompensa = reward(resultado == "User", resultado == "IA")
        update_Q(estado_actual, carta_ia, recompensa, nuevo_estado, mano_ia)
        
        ganador = verificar_condicion_victoria(victorias)
        if ganador:
            print(f"\n{ganador} ha ganado el juego!")
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

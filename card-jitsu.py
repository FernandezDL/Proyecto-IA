from asignarCartas import cargar_cartas, asignar_cartas
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
        if all(len(set(colores)) >= 1 for colores in elementos.values()) and len(set.union(*(set(colores) for colores in elementos.values()))) == 3:
            return jugador
        # Verificar victoria por tres colores únicos en un solo elemento
        for colores in elementos.values():
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

        eleccion_ia = random.randint(0, 4)
        carta_ia = mano_ia.pop(eleccion_ia)
        print(f"\nUsuario: {carta_user}")
        print(f"IA: {carta_ia}")

        resultado = determinar_ganador(carta_user, carta_ia, victorias)
        if resultado == "Empate":
            print(resultado)
        else:
            print(f"Victoria para: {resultado}")

        mostrar_victorias(victorias)

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

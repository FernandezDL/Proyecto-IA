import numpy as np
import random

acciones = ["Fuego", "Agua", "Nieve"]

def elegir_accion(Q, estado):
    rand = random.randint(0,2)
    return acciones[rand]


alpha = 0.1 
gamma = 0.9 
epsilon = 0.1 

Q = np.random.rand(3, 3)  

victorias_usuario = {"Fuego": 0, "Agua": 0, "Nieve": 0}
victorias_agente = {"Fuego": 0, "Agua": 0, "Nieve": 0}

while True:
    accion = elegir_accion(Q, 0)

    # El usuario elige una acción (carta)
    accion_usuario = input("Elige una carta (Fuego, Agua, Nieve): ")
    while accion_usuario not in acciones:
        print("Carta inválida. Por favor, elige una de las siguientes cartas: Fuego, Agua, Nieve")
        accion_usuario = input("Elige una carta (Fuego, Agua, Nieve): ")

    print("El agente elige:", accion)

    if accion == accion_usuario:
        print("Empate")
        recompensa = 0
    elif (accion == "Fuego" and accion_usuario == "Nieve") or \
         (accion == "Agua" and accion_usuario == "Fuego") or \
         (accion == "Nieve" and accion_usuario == "Agua"):
        print("¡El agente gana!")
        recompensa = 1
        victorias_agente[accion] += 1
    else:
        print("¡El agente pierde!")
        recompensa = -1
        victorias_usuario[accion_usuario] += 1

    Q[0, acciones.index(accion)] += alpha * (recompensa + gamma * np.max(Q[:, acciones.index(accion)]) - Q[0, acciones.index(accion)])

    print("Conteo de victorias del usuario:")
    print(victorias_usuario)
    print("Conteo de victorias del agente:")
    print(victorias_agente)
    print()

    if (any(v >= 3 for v in victorias_usuario.values()) or any(v >= 3 for v in victorias_agente.values())) \
            or all(v > 0 for v in victorias_usuario.values()) or all(v > 0 for v in victorias_agente.values()):
        print("¡Fin del juego!")
        break

print("El juego ha terminado.")

import numpy as np
import random
import pickle

Q = {}
alpha = 0.5
gamma = 0.9
epsilon = 0.1

def inicializar_Q():
    global Q
    try:
        with open('q_table.pkl', 'rb') as f:
            Q = pickle.load(f)
    except FileNotFoundError:
        Q = {}

def guardar_q_table():
    with open('q_table.pkl', 'wb') as f:
        pickle.dump(Q, f)

# Función obtener estado
def get_state(victorias, mano_ia, mazo_user, mazo_ia, historial_acciones):
    # Número de victorias por cada elemento
    estado_victorias_ia = tuple(len(victorias["IA"][elemento]) for elemento in ['Fuego', 'Agua', 'Nieve'])
    estado_victorias_user = tuple(len(victorias["User"][elemento]) for elemento in ['Fuego', 'Agua', 'Nieve'])
    
    # Número de cartas de cada elemento en la mano de la IA
    conteo_cartas_ia = {'Fuego': 0, 'Agua': 0, 'Nieve': 0}
    for carta in mano_ia:
        conteo_cartas_ia[carta.elemento] += 1
    estado_cartas_ia = (conteo_cartas_ia['Fuego'], conteo_cartas_ia['Agua'], conteo_cartas_ia['Nieve'])
    
    # Número total de cartas restantes en los mazos de ambos jugadores
    num_cartas_restantes = (len(mazo_user), len(mazo_ia))
    
    # Resumen del historial de acciones recientes (por ejemplo, las últimas 3 acciones)
    resumen_historial = tuple(historial_acciones[-3:])

    # Combinar toda la información relevante en el estado simplificado
    return estado_victorias_ia + estado_victorias_user + estado_cartas_ia + num_cartas_restantes + resumen_historial



# Función de recompensa
def reward(user_win, ia_win):
    if ia_win:
        return 1  
    elif user_win:
        return -1 
    return -0.1 

# Actualización de Q
def update_Q(state, action, reward, next_state, all_possible_actions):
    current_q = Q.get((state, action), 0)
    max_future_q = max([Q.get((next_state, a), 0) for a in all_possible_actions])
    Q[(state, action)] = current_q + alpha * (reward + gamma * max_future_q - current_q)

# Selección de acción basada en Q
def select_action(state, possible_actions):
    if np.random.rand() < epsilon:  # Exploración con una probabilidad del 10%
        return np.random.choice(possible_actions)
    q_values = [Q.get((state, action), 0) for action in possible_actions]
    max_q = max(q_values)
    # Si hay varias acciones con el mismo Q máximo, elige una al azar entre ellas
    best_actions = [action for action, q in zip(possible_actions, q_values) if q == max_q]
    return np.random.choice(best_actions)

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
    estado_ia = tuple((elemento, tuple(victorias["IA"][elemento])) for elemento in ['Fuego', 'Agua', 'Nieve'])
    estado_user = tuple((elemento, tuple(victorias["User"][elemento])) for elemento in ['Fuego', 'Agua', 'Nieve'])
    cartas = tuple(sorted((carta.elemento, carta.numero) for carta in mano_ia))
    num_cartas_restantes = (len(mazo_user), len(mazo_ia))
    return estado_ia + estado_user + cartas + num_cartas_restantes + historial_acciones



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

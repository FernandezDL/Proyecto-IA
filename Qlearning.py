import numpy as np

def get_state(victorias, mano_ia):
    """Genera una tupla que representa el estado actual del juego desde la perspectiva de la IA."""
    estado = tuple((elemento, tuple(victorias["IA"][elemento])) for elemento in ['Fuego', 'Agua', 'Nieve'])
    cartas = tuple(sorted((carta.elemento, carta.numero) for carta in mano_ia))
    return estado + cartas

# Función de recompensa
def reward(user_win, ia_win):
    if ia_win:
        return 1  # Recompensa positiva si gana la IA
    elif user_win:
        return -1  # Recompensa negativa si gana el usuario
    return -0.1  # Pequeña penalización por empate

# Inicialización de la tabla Q
Q = {}

# Definición de parámetros de aprendizaje
alpha = 0.5
gamma = 0.9

# Actualización de Q
def update_Q(state, action, reward, next_state, all_possible_actions):
    current_q = Q.get((state, action), 0)
    max_future_q = max([Q.get((next_state, a), 0) for a in all_possible_actions])
    Q[(state, action)] = current_q + alpha * (reward + gamma * max_future_q - current_q)

# Selección de acción basada en Q
def select_action(state, possible_actions):
    if np.random.rand() < 0.1:  # Exploración con una probabilidad del 10%
        return np.random.choice(possible_actions)
    q_values = [Q.get((state, action), 0) for action in possible_actions]
    max_q = max(q_values)
    # Si hay varias acciones con el mismo Q máximo, elige una al azar entre ellas
    best_actions = [action for action, q in zip(possible_actions, q_values) if q == max_q]
    return np.random.choice(best_actions)

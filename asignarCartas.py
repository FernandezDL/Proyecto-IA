import json
import random

class Carta:
    def __init__(self, color, numero, elemento, image):
        self.color = color
        self.numero = numero
        self.elemento = elemento
        self.image = image

    def __repr__(self):
        return f'Carta(Color: {self.color}, Número: {self.numero}, Elemento: {self.elemento})'

def cargar_cartas():
    """Cargar las cartas desde el archivo JSON y devolver una lista de cartas"""
    with open('cartas.json', 'r') as archivo:
        cartas_data = json.load(archivo)
        cartas = [Carta(**datos) for datos in cartas_data]
        return cartas

def asignar_cartas(cartas):
    """Asignar cartas aleatoriamente a dos jugadores permitiendo duplicados entre sets"""
    cantidad_por_elemento = 10
    cartas_user = []
    cartas_ia = []
    cartas_por_elemento = {'Fuego': [], 'Agua': [], 'Nieve': []}
    
    for carta in cartas:
        cartas_por_elemento[carta.elemento].append(carta)
    
    for elemento, lista_cartas in cartas_por_elemento.items():
        cartas_user.extend(random.sample(lista_cartas, min(cantidad_por_elemento, len(lista_cartas))))
        cartas_ia.extend(random.sample(lista_cartas, min(cantidad_por_elemento, len(lista_cartas))))
    
    return cartas_user, cartas_ia

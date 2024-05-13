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
    """ Cargar las cartas desde el archivo JSON y agruparlas por elemento """
    with open('cartas.json', 'r') as archivo:
        cartas_data = json.load(archivo)
        cartas = [Carta(**datos) for datos in cartas_data]
        cartas_por_elemento = {'Fuego': [], 'Agua': [], 'Nieve': []}
        for carta in cartas:
            cartas_por_elemento[carta.elemento].append(carta)
        return cartas_por_elemento

def asignar_cartas(cartas):
    """ Asignar cartas aleatoriamente a dos jugadores permitiendo duplicados entre sets """
    cantidad_por_elemento = 10
    cartas_user = []
    cartas_ia = []
    for elemento, lista_cartas in cartas.items():
        cartas_user.extend(random.sample(lista_cartas, cantidad_por_elemento))
        cartas_ia.extend(random.sample(lista_cartas, cantidad_por_elemento))
    return cartas_user, cartas_ia
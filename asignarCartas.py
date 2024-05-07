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
    """ Cargar las cartas desde el archivo JSON """
    with open('cartas.json', 'r') as archivo:
        cartas_data = json.load(archivo)
        return [Carta(**datos) for datos in cartas_data]

def asignar_cartas(cartas):
    """ Asignar cartas aleatoriamente a dos jugadores permitiendo duplicados entre sets """
    cartas_user = random.choices(cartas, k=30)
    cartas_ia = random.choices(cartas, k=30)
    return cartas_user, cartas_ia
import json
import random

class Carta:
    def __init__(self, color, numero, elemento):
        self.color = color
        self.numero = numero
        self.elemento = elemento

    def __repr__(self):
        return f'Carta(Color: {self.color}, Número: {self.numero}, Elemento: {self.elemento})'

def cargar_cartas():
    """ Cargar las cartas desde el archivo JSON """
    with open('cartas.json', 'r') as archivo:
        cartas_data = json.load(archivo)
        return [Carta(**datos) for datos in cartas_data]

def asignar_cartas(cartas):
    """ Asignar cartas aleatoriamente a dos jugadores asegurando que no haya duplicados en cada set """
    random.shuffle(cartas)  # Mezclar todas las cartas para asegurar aleatoriedad
    cartas_user = cartas[:30]  # Las primeras 30 cartas para el usuario
    cartas_ia = cartas[30:60]  # Las siguientes 30 cartas para la IA
    return cartas_user, cartas_ia
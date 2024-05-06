import json
import random

class Carta:
    colores = ['Azul', 'Verde', 'Naranja', 'Lila', 'Rojo', 'Amarillo']
    elementos = ['Fuego', 'Agua', 'Nieve']
    numeros = [3] + [4, 5, 6, 7, 8, 9]*2 + [10, 11, 12] 

    def __init__(self):
        self.color = random.choice(Carta.colores)
        self.numero = random.choice(Carta.numeros)
        self.elemento = random.choice(Carta.elementos)

    def __repr__(self):
        return f'Carta(Color: {self.color}, Número: {self.numero}, Elemento: {self.elemento})'

def crear_cartas(n):
    return [Carta() for _ in range(n)]

n = 150  
cartas = crear_cartas(n)

cartas_json = json.dumps([{'color': carta.color, 'numero': carta.numero, 'elemento': carta.elemento} for carta in cartas], indent=4)

with open('cartas.json', 'w') as archivo:
    archivo.write(cartas_json)



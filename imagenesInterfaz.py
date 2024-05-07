from io import BytesIO
import os
import pygame
import requests

pygame.font.init()  # Inicializar el módulo de fuentes
font_size = 35 
font = pygame.font.Font(None, font_size)

def cargar_marcos(card_size):
    marcos = {}
    colores = ['Azul', 'Verde', 'Lila', 'Rojo', 'Amarillo', 'Naranja'] 
    for color in colores:
        path_marco = os.path.join('images', f'{color.lower()}.png')
        marco = pygame.image.load(path_marco)
        marco = pygame.transform.scale(marco, card_size)  
        marcos[color] = marco
    return marcos
    
def cargar_elementos(element_size):
    elementos = {}
    tipos = ['Fuego', 'Nieve', 'Agua'] 
    for tipo in tipos:
        path_elemento = os.path.join('images', f'{tipo.lower()}.png')
        elemento = pygame.image.load(path_elemento)
        elemento = pygame.transform.scale(elemento, element_size) 
        elementos[tipo] = elemento
    return elementos

def load_card_images(hand, marcos, elementos, card_size):
    card_images = []
    for card in hand:
        img_url = card.image
        response = requests.get(img_url)
        image = pygame.image.load(BytesIO(response.content))
        image = pygame.transform.scale(image, card_size)

        # Aplicar el marco correspondiente
        color = card.color
        marco = marcos[color]
        image.blit(marco, (0, 0))  # Aplica el marco sobre la imagen de la carta

        # Renderizar el elemento en la esquina superior izquierda
        tipo = card.elemento
        elemento= elementos[tipo]
        image.blit(elemento, (5,5))

        # Renderizar el número en la esquina superior izquierda
        texto = font.render(str(card.numero), True, (0,0,0))  
        image.blit(texto, (10, 25))

        card_images.append(image)
    return card_images
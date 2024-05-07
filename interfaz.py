import pygame
import json
import requests
from pygame.locals import *
import os
from imagenesInterfaz import cargar_marcos, load_card_images, cargar_elementos
from asignarCartas import cargar_cartas, asignar_cartas
from cardJitsu import seleccionar_cartas_mano

pygame.init()

width, height = 1000, 600
card_size = (100, 120) 
element_size = (20, 20)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Card-Jitsu')

background_image_path = os.path.join('images', 'dojo.png')
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (width, height))

sound = pygame.mixer.Sound("music/cardJitsu.mp3")
# sound.play(-1)

cartas = cargar_cartas()
cartas_user, cartas_ia = asignar_cartas(cartas)
mano_user, mazo_user = seleccionar_cartas_mano(cartas_user)
mano_ia, mazo_ia = seleccionar_cartas_mano(cartas_ia)

#Cartas
marcos = cargar_marcos(card_size)
elementos = cargar_elementos(element_size)
card_images = load_card_images(mano_user, marcos, elementos, card_size)

# Variables de control
running = True

# Posiciones de las cartas en pantalla
card_positions = [(50 + i * (card_size[0] + 10), height - card_size[1] - 50) for i in range(len(card_images))]

def draw_cards():
    screen.blit(background_image, (0, 0))
    for idx, img in enumerate(card_images):
        screen.blit(img, card_positions[idx])
    pygame.display.flip()

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for idx, pos in enumerate(card_positions):
                rect = pygame.Rect(pos, card_size)
                if rect.collidepoint(x, y):
                    print(f"Has seleccionado la carta: {mano_user[idx]}")
                    # Aquí podrías manejar la lógica para jugar la carta seleccionada

    draw_cards()
   
# Cerrar Pygame
pygame.quit()

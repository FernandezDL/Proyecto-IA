import pygame
import json
import requests
from pygame.locals import *
import os
from cardJitsu import cargar_cartas, asignar_cartas, seleccionar_cartas_mano

pygame.init()

width, height = 1000, 600
card_size = (100, 150) 

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Card-Jitsu')

background_image_path = os.path.join('images', 'dojo.png')
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (width, height))

sound = pygame.mixer.Sound("music/cardJitsu.mp3")
sound.play()

# Variables de control
running = True

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()

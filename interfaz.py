import pygame
import requests
from pygame.locals import *
import os
import imagenesInterfaz
from asignarCartas import cargar_cartas, asignar_cartas
import cardJitsu as cj
import random

pygame.init()

width, height = 1000, 600
card_size = (100, 120) 
element_size = (20, 20)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Card-Jitsu')

background_image_path = os.path.join('images', 'dojo.png')
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (width, height))
screen.blit(background_image, (0, 0))

#Sonido del juego
sound = pygame.mixer.Sound("music/cardJitsu.mp3")
# sound.play(-1)

#Selección de cartas
cartas = cargar_cartas()
cartas_user, cartas_ia = asignar_cartas(cartas)
mano_user, mazo_user = cj.seleccionar_cartas_mano(cartas_user)
mano_ia, mazo_ia = cj.seleccionar_cartas_mano(cartas_ia)

#Visuales de las cartas
marcos = imagenesInterfaz.cargar_marcos(card_size)
elementos = imagenesInterfaz.cargar_elementos(element_size)
card_images = imagenesInterfaz.load_card_images(mano_user, marcos, elementos, card_size)
card_positions = [(50 + i * (card_size[0] + 10), height - card_size[1] - 50) for i in range(len(card_images))]

# Variables de control
running = True

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
                    carta_user= mano_user.pop(idx)

                    carta_ia = mano_ia.pop(random.randint(0, 4))
                    print(f"IA: {carta_ia}")

                    juegoTermiando, ganador, victorias= cj.jugar(carta_user, carta_ia)

                    #Actualizar mazos, manos y visuales
                    mazo_ia, mazo_user, mano_ia, mano_user = cj.cambiar_carta(mazo_ia, mazo_user, mano_ia, mano_user)
                    card_images = imagenesInterfaz.load_card_images(mano_user, marcos, elementos, card_size)

                    #Iconos ganadores
                    iconos= imagenesInterfaz.iconos_victorias()
                    imagenesInterfaz.draw_victories(screen, victorias, iconos, 10, width - 100, 10)  # Ajusta las coordenadas según sea necesario

                    print(juegoTermiando)
                    if juegoTermiando:
                        imagenesInterfaz.mostrar_mensaje_ganador(screen, ganador, width, height)
                        running = False

    imagenesInterfaz.draw_cards(screen, card_images, card_positions)
   
# Cerrar Pygame
pygame.quit()

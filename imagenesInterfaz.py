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

def draw_cards(screen, card_images, card_positions):
    for idx, img in enumerate(card_images):
        screen.blit(img, card_positions[idx])
    pygame.display.flip()

def iconos_victorias():
    iconos = {}

    # Elementos y colores
    elementos = ['Fuego', 'Nieve', 'Agua'] 
    colores = ['Azul', 'Verde', 'Lila', 'Rojo', 'Amarillo', 'Naranja'] 

    # Cargar los fondos de cada color
    fondos = {color: pygame.transform.scale(pygame.image.load(os.path.join('images', f'icon_{color.lower()}.png')), (40, 40)) for color in colores}

    # Cargar y redimensionar los iconos de elementos a un tamaño más pequeño basado en el tamaño fijo del fondo
    elementos_iconos = {
        elemento: pygame.transform.scale(
            pygame.image.load(os.path.join('images', f'{elemento.lower()}.png')),
            (int(100 // 3), int(100 // 3))  # 1/3 del tamaño del fondo
        ) for elemento in elementos
    }
    
    for elemento in elementos:
        iconos[elemento] = {}
        for color in colores:
            # Copia del fondo para evitar modificar el original
            fondo = fondos[color].copy()
            
            # Obtener el icono del elemento ya redimensionado
            icono_elemento = elementos_iconos[elemento]
            
            # Calcular la posición centrada para el icono en el fondo
            posicion = ((fondo.get_width() - icono_elemento.get_width()) // 2,
                        (fondo.get_height() - icono_elemento.get_height()) // 2)
            
            # Combinar el icono del elemento con el fondo
            fondo.blit(icono_elemento, posicion)
            iconos[elemento][color] = fondo

    return iconos

def draw_victories(screen, victorias, iconos, start_left, start_right, y_start):
    offset = 5  # Espacio entre iconos
    column_width = 50  # Ancho de cada columna de iconos

    # Dibujar victorias de la IA en la esquina superior izquierda
    for idx, elemento in enumerate(['Fuego', 'Agua', 'Nieve']):
        x = start_left + idx * column_width
        y = y_start
        for color in victorias['IA'][elemento]:
            screen.blit(iconos[elemento][color], (x, y))
            y += iconos[elemento][color].get_height() + offset

    # Dibujar victorias del usuario en la esquina superior derecha
    for idx, elemento in enumerate(['Fuego', 'Agua', 'Nieve']):
        x = start_right - idx * column_width
        y = y_start
        for color in victorias['User'][elemento]:
            screen.blit(iconos[elemento][color], (x, y))
            y += iconos[elemento][color].get_height() + offset

def mostrar_mensaje_ganador(screen, ganador, width, height):
    # Definir visuales
    color_fondo = (0, 122, 204)
    color_boton = (255, 255, 255)  
    fuente = pygame.font.Font(None, 36)
    fuente_boton = pygame.font.Font(None, 28)

    # rectángulos
    rect_fondo = pygame.Rect(width // 2 - 150, height // 2 - 60, 300, 120)
    rect_boton = pygame.Rect(width // 2 - 50, height // 2 + 10, 100, 40)
    
    # Dibujar fondo y botón
    border_radius = 15
    pygame.draw.rect(screen, color_fondo, rect_fondo, border_radius=border_radius)
    pygame.draw.rect(screen, color_boton, rect_boton, border_radius=border_radius)

    # Colocar texto
    texto = fuente.render(f"{ganador} Wins", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(width // 2, height // 2 - 20))
    texto_boton = fuente_boton.render("OK", True, (0, 0, 0))
    texto_boton_rect = texto_boton.get_rect(center=(width // 2, height // 2 + 30))
    
    screen.blit(texto, texto_rect)
    screen.blit(texto_boton, texto_boton_rect)
    pygame.display.flip()

    # Esperar a que el usuario presione el botón OK
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if rect_boton.collidepoint(mouse_x, mouse_y):
                    waiting_for_key = False
            if event.type == pygame.QUIT:
                waiting_for_key = False
                pygame.quit()
                return

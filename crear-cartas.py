import json
from cards import cards  # Asegúrate de que el archivo cards.py esté en el mismo directorio que este script

# Convertir el diccionario de cartas al formato deseado
new_cards = []
for card_id, card_info in cards.items():
    new_card = {
        "color": card_info['colour'].capitalize(),  # Cambia el color a mayúscula inicial
        "numero": card_info['power'],
        "elemento": card_info['element'].capitalize(),  # Cambia el elemento a mayúscula inicial
        "image" : card_info['image']
    }
    new_cards.append(new_card)

# Guardar el nuevo diccionario en un archivo JSON
with open('cartas.json', 'w') as json_file:
    json.dump(new_cards, json_file, indent=4)

print("El archivo JSON ha sido creado exitosamente.")

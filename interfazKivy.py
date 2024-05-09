from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import os

# Configura las dimensiones de la ventana
Window.size = (800, 600)

class CardJitsuApp(App):
    def build(self):
        # Crea un widget que será el contenedor principal
        self.root = Widget()

        # Establece la imagen de fondo
        with self.root.canvas.before:
            self.bg = Rectangle(source=os.path.join('images', 'dojo.png'), pos=self.root.pos, size=Window.size)

        # Cargar sonido
        self.sound = SoundLoader.load('music/cardJitsu.mp3')
        if self.sound:
            self.sound.loop = True  # Hace que el sonido se repita indefinidamente
            self.sound.play()
        else:
            print("No se pudo cargar el archivo de sonido.")


        # Cargar cartas y manejar la lógica del juego aquí
        # ...

        return self.root

    def on_start(self):
         # Detener el sonido cuando la aplicación se cierre
        if self.sound:
            self.sound.stop()

if __name__ == '__main__':
    CardJitsuApp().run()

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

class CardJitsu(App):
    def build(self):
        self.layout = FloatLayout()

        # -------------------- Fondo --------------------
        bg_image = Image(source='images/dojo.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(bg_image)

        # -------------------- Musica --------------------
        self.sound = SoundLoader.load('music/cardJitsu.mp3')
        if self.sound:
            self.sound.loop = True  # Hace que la música se repita continuamente
            self.sound.play()

        # -------------------- Animacion de los pinguinos --------------------
        self.img = Image(source='images/pinguinos/pinguinos1.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.img)  # Asegúrate de añadir este widget al layout

        self.images = [f'images/pinguinos/pinguinos{i}.png' for i in range(1, 8)]
        self.current_index = 0

        # Cambio de imagen
        Clock.schedule_interval(self.next_image, 0.3)

        return self.layout

    def next_image(self, dt):
        self.current_index = (self.current_index + 1) % len(self.images)
        
        # Cambiar la imagen
        self.img.source = self.images[self.current_index]

if __name__ == '__main__':
    CardJitsu().run()

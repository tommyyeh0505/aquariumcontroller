from kivy.app import App
from aquariumcontroller import AquariumController
from ledcomponent import LEDComponent
from componentcontroller import ComponentController

class AquariumControllerApp(App):


    def build(self):
        self.ac = AquariumController()
        leds = [LEDComponent(23)]
        self.controller = ComponentController(leds)
        return self.ac
    
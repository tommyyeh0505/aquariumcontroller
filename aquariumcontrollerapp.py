from kivy.app import App
from aquariumcontroller import AquariumController
<<<<<<< HEAD
from ledcomponent import LEDComponent
from componentcontroller import ComponentController

class AquariumControllerApp(App):


    def build(self):
        self.ac = AquariumController()
        leds = [LEDComponent(23)]
        self.controller = ComponentController(leds)
        return self.ac
    
=======

class AquariumControllerApp(App):
	ac = AquariumController()

	def build(self):
		ac = AquariumController()
		return ac
	
>>>>>>> 610e980f517f05b8c41ad0c709b0d12a525f9ea5

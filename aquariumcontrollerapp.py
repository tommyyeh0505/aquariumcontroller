from kivy.app import App
from aquariumcontroller import AquariumController

class AquariumControllerApp(App):
	ac = AquariumController()

	def build(self):
		ac = AquariumController()
		return ac
	
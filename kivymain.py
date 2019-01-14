import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class AquariumController(GridLayout):
    pass
    
class AquariumControllerApp(App):
    def build(self):
        return AquariumController()
        
aquariumController = AquariumControllerApp()
aquariumController.run()
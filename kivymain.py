import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
from threading import Thread
import time


kivy.require("1.9.0")

from aquariumcontrollerapp import AquariumControllerApp
from aquariumcontroller import AquariumController

aquariumController = AquariumControllerApp()

def continuousUpdateTemp():
    
    #ensure cycle starts after app is initialized to prevent
    time.sleep(2)

    while True:
        time.sleep(0.1)
        aquariumController.ac.updateCurrentTemp()
        
t = Thread(target = continuousUpdateTemp)    
t.daemon = True
t.start()
t.join
aquariumController.run()

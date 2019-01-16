import os
#os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
from threading import Thread
import time


kivy.require("1.9.0")

from aquariumcontrollerapp import AquariumControllerApp
from aquariumcontroller import AquariumController
<<<<<<< HEAD

aquariumController = AquariumControllerApp()

def continuousUpdateTemp():
    
    #ensure cycle starts after app is initialized to prevent
    time.sleep(2)

    while True:
        time.sleep(0.1)
        aquariumController.ac.updateCurrentTemp()
        
=======

aquariumController = AquariumControllerApp()

def continuousUpdateTemp():
	while True:
		time.sleep(0.5)
		aquariumController.ac.updateCurrentTemp()
		
>>>>>>> 610e980f517f05b8c41ad0c709b0d12a525f9ea5
t = Thread(target = continuousUpdateTemp)    
t.daemon = True
t.start()
t.join
aquariumController.run()

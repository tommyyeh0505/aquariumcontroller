import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import StringProperty



class AquariumController(GridLayout):
    defaultTemp = 20.0
    defaultFlow = 100
    defaultLight = 50
    
    
    set_temp_label = StringProperty(str(defaultTemp) + "F")
    set_flow_label = StringProperty(str(defaultFlow) + "GPH")
    set_light_label = StringProperty(str(defaultLight) + "%")
    current_temp_label = StringProperty("Measuring")
    
    def updateTemp(self, value):
        temperature = str(value) + "F"
        self.set_temp_label = temperature
        print("Temp: " + temperature)

    def updateCurrentTemp(self, value):
        temperature = str(value) + "F"
        self.current_temp_label = temperature
        print("Current Temp: " + temperature)
        
    def updateFlow(self, value):
        flow = str(int(value)) + "GPH"
        self.set_flow_label = flow
        print("Flow: " + flow)
        
    def updateLight(self, value):
        lightIntensity = str(int(value)) + "%"
        self.set_light_label = lightIntensity
        print("Light: " + lightIntensity)   

    # -------- TEMP SENSOR
    def sensor(self):
        for i in os.listdir('/sys/bus/w1/devices'):
            if i != 'w1_bus_master1':
                ds18b20 = i
        return ds18b20

    def read(self, ds18b20):
        location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        celsius = temperature / 1000
        farenheit = (celsius * 1.8) + 32
        return celsius, farenheit
        
    def __init__(self):
        super(AquariumController, self).__init__()
        tempSensorSerialNum = self.sensor()
        print ("Serial Num" + tempSensorSerialNum)
        self.updateTemp(self.defaultTemp)
        self.updateFlow(self.defaultFlow)
        self.updateLight(self.defaultLight)
        currentTemp = self.read(tempSensorSerialNum)[1]
        print(currentTemp)
        self.updateCurrentTemp(str(currentTemp) + "F")    
        
        
class AquariumControllerApp(App):
    def build(self):
        return AquariumController()
    
        
aquariumController = AquariumControllerApp()
aquariumController.run()



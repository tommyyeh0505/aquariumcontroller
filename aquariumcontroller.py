import kivy
import os
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
		#print("Temp: " + temperature)

	def setCurrentTemp(self, value):
		temperature = str(value) + "F"
		self.current_temp_label = temperature
		#print("Current Temp: " + temperature)
		
	def updateCurrentTemp(self):
		try:
			print(self.sensor()[1])
			temperature = str(self.read(self.tempSensorSerialNum)[1]) + "F"
			self.current_temp_label = temperature
			print("UCurrent Temp: " + temperature)
		except Exception as e:
			print("Updated")
		
	def updateFlow(self, value):
		flow = str(int(value)) + "GPH"
		self.set_flow_label = flow
		#print("Flow: " + flow)
		
	def updateLight(self, value):
		lightIntensity = str(int(value)) + "%"
		self.set_light_label = lightIntensity
		#print("Light: " + lightIntensity)   

	# -------- TEMP SENSOR
	def sensor(self):
		try:
			for i in os.listdir('/sys/bus/w1/devices'):
				if i != 'w1_bus_master1':
					ds18b20 = i
			return ds18b20
		except FileNotFoundError as e:
			return 0
		

	def read(self, ds18b20):

		try:
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
		except BaseException as e:
			return 0, 0



	def __init__(self):
		super(AquariumController, self).__init__()
		self.tempSensorSerialNum = self.sensor()
		
		self.updateTemp(self.defaultTemp)
		self.updateFlow(self.defaultFlow)
		self.updateLight(self.defaultLight)
		
		currentTemp = self.read(self.tempSensorSerialNum)[1]
		self.setCurrentTemp(str(currentTemp) + "F")
		
		
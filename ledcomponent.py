import RPi.GPIO as GPIO
from time import sleep


class LEDComponent():
    
    def __init__(self, pin_number):
        self.pin_number = pin_number
    


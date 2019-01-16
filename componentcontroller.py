import RPi.GPIO as GPIO
from ledcomponent import LEDComponent

class ComponentController():

    
    def __init__(self, led_list):
        self.led_list = led_list
        GPIO.setmode(GPIO.BCM)
        self.led_pwm = []
        for i in led_list:
            print(i.pin_number)
            GPIO.setup(i.pin_number, GPIO.OUT)
            pwm = GPIO.PWM(i.pin_number,100)
            pwm.start(100)
            self.led_pwm.append(pwm)
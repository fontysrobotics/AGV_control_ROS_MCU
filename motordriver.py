import board 
import time 
from digitalio import DigitalInOut, Direction, Pull

class MD13S:

    def __init__(self, PWM_pin, dir_pin, feedback_pin):

        self.PWMpin = PWM_pin
        self.DirPin = dir_pin
        self._feedback = DigitalInOut(feedback_pin)
    

    def speed_control(self, speedvector):



    def get_motor_speed(self):


       

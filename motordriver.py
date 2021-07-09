import board 
from digitalio import DigitalInOut, Direction
from pwmio import PWMOut

class MD13S:
# Encoder resolution: 48 counts per motor shaft revolution
# Gear ratio: 30:1

    def __init__(self, PWM_pin, dir_pin):
        self._PWMpin = PWM_pin
        self._DirPin = DigitalInOut(dir_pin)
        self._DirPin.direction = Direction.OUTPUT
        self._pwm = PWMOut(PWM_pin)
        self.last_position = None
    

    def speed_control(self, speedvector):
        self._pwm.duty_cycle = speedvector

    def direction_control(self,direction):
        self._DirPin.value = direction

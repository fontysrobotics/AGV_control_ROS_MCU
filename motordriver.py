import board 
import time 
from digitalio import DigitalInOut, Direction, Pull
import rotaryio
from pwmio import PWMOut
import math

class MD13S:
# Encoder resolution: 48 counts per motor shaft revolution
# Gear ratio: 30:1

    def __init__(self, PWM_pin, dir_pin):

        self._PWMpin = PWM_pin
        self._DirPin = DigitalInOut(dir_pin)
        self._DirPin.direction = Direction.OUTPUT
        # self._encPinA = enc_pin_A
        # self._encPinB = enc_pin_B
        # self._motorSP = motor_setpoint
        # self._feedback = rotaryio.IncrementalEncoder(enc_pin_A, enc_pin_B)
        self._pwm = PWMOut(PWM_pin)
        self.last_position = None
    

    def speed_control(self, speedvector):
        self._pwm.duty_cycle = speedvector

    def direction_control(self,direction):
        self._DirPin.value = direction
        
    def get_motor_speed(self):
        position = self._feedback.position
        if self.last_position == None:
            print(1, position)

        if position != self.last_position:
            print(2, position)

        self.last_position = position
        print(3, position)

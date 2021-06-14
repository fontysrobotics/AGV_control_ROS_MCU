import board 
import time 
from digitalio import DigitalInOut, Direction, Pull
import rotaryio
from pwmio import PWMOut
import math

class MD13S:
# Encoder resolution: 48 counts per motor shaft revolution
# Gear ratio: 30:1

    def __init__(self, PWM_pin, dir_pin, enc_pin_A, enc_pin_B, motor_setpoint):

        self.PWMpin = PWM_pin
        self.DirPin = dir_pin
        self.encPinA = enc_pin_A
        self.encPinB = enc_pin_B
        self.motorSP = motor_setpoint
        self._feedback = rotaryio.IncrementalEncoder(enc_pin_A, enc_pin_B)
        self._pwm = PWMOut(PWM_pin, frequency=5000, duty_cycle=0)
    

    def speed_control(self, speedvector):
        self._pwm.duty_cycle = motor_setpoint - 
        

    def get_motor_speed(self):
        speed = self._feedback.position/48 # omw

import board 
import time 
from digitalio import DigitalInOut, Direction, Pull
import rotaryio
from pwmio import PWMOut
import math

class motor_enc():
# Encoder resolution: 48 counts per motor shaft revolution
# Gear ratio: 30:1

    def __init__(self, enc_pin_A, enc_pin_B):
        # self.encoder = rotaryio.IncrementalEncoder(enc_pin_A, enc_pin_B)
        self.count = 0
        self.position = 0
        self.last_position = -1

        self.enc_a = DigitalInOut(enc_pin_A)
        self.enc_a.direction = Direction.INPUT
        self.enc_b = DigitalInOut(enc_pin_B)
        self.enc_b.direction = Direction.INPUT
    
        
    def get_motor_speed(self):
        self.position = self.enc_a.value
        if self.position != self.last_position:
            if (self.enc_b.value != self.position):
                self.count = self.count + 1
            else:
                self.count = self.count - 1
        self.last_position = self.position
        return self.count

class odom_calc():
    def __init__(self):
        self.time_last = time.time()
        self.old_counter_1 = 0
        self.old_counter_2 = 0

    def Odometry(self, counter_1, counter_2):
        time_now = time.time()
        
        delta_vel_right = ((counter_1 - self.old_counter_1) * 2 * math.pi * 0.05 / 64)/(time_now-self.time_last) # 0.05m = wheel radius, 64 = encoder steps
        delta_vel_left = ((counter_2 - self.old_counter_2) * 2 * math.pi * 0.05 / 64)/(time_now-self.time_last)
        
        self.old_counter_1 = counter_1
        self.old_counter_2 = counter_2
        self.time_last = time_now
        
        delta_vel_center = (delta_vel_right + delta_vel_left) / 2
        delta_ang_center = delta_vel_center / 0.05
        return delta_vel_center, delta_ang_center
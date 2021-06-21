import time
import board
import math
from digitalio import DigitalInOut, Direction
#import IRsensor
import adafruit_hcsr04
import motordriver
#import Temperature
#import BMS
#from pwmio import PWMOut
from i2c import i2c_bus
import rotaryio
import pulseio

'''
#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.IRsensor(board.A14)
IRsensorRear = IRsensor.IRsensor(board.A15)
'''
#instances ultrasonic sensors sides
# USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)
# USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D8)
# USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.D30, echo_pin=board.D31)
# USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.D28, echo_pin=board.D29)

# try:
#     print(1, USsensorFL.distance)
# except RuntimeError:
#     pass
'''
# Fans
FanPWM = PWMOut(pin = board.D3, frequency=5000, duty_cycle=0)
'''

if __name__ == '__main__':
    pass
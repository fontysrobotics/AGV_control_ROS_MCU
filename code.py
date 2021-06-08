import time
import board 
import math 
import IRsensor
import adafruit_hcsr04
import motordriver
import fan 
import Temperature
import BMS
from pwmio import PWMOut

#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.IRsensor(board.A14)
IRsensorRear = IRsensor.IRsensor(board.A15)

#instances ultrasonic sensors sides
USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D34, echo_pin=board.D35)
USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D32, echo_pin=board.D33)
USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.D30, echo_pin=board.D31)
USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.D28, echo_pin=board.D29)

# Fans
FanPWM = PWMOut(pin = board.D3, frequency=5000, duty_cycle=0)





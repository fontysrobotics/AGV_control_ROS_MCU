import time
import board
import math
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import IRsensor
import adafruit_hcsr04
import motordriver
import supervisor
#import Temperature
#import BMS
#from pwmio import PWMOut
from i2c import i2c_bus
import rotaryio


#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.IRsensor(board.A1)
IRsensorRear = IRsensor.IRsensor(board.A0)

#instances ultrasonic sensors sides
USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D4)
# USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.D30, echo_pin=board.D31)
# USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.D28, echo_pin=board.D29)

# while True:
    # try:
    #     print(1, USsensorFL.distance)
    # except RuntimeError:
    #     pass
'''
# Fans
FanPWM = PWMOut(pin = board.D3, frequency=5000, duty_cycle=0)
'''
def readSerial():
     if (supervisor.runtime.serial_bytes_available):
        value = input().strip()
        value = float(value)
        if value == "":
            pass
            
sonar1 = 0
sonar2 = 0
while True:
    readSerial()
    ir_back = IRsensorRear.get_distance_IR()
    ir_front = IRsensorFront.get_distance_IR()
    try:
        sonar1 = USsensorFR.distance/100
    except RuntimeError:
        sonar1 = sonar1/100
    try:
        sonar2 = USsensorFL.distance/100
    except RuntimeError:
        sonar2 = sonar2/100
        

    print(ir_back, ir_front, sonar1, sonar2)

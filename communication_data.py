import time
import board
import math
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import IRsensor
import adafruit_hcsr04
import motordriver
import supervisor
from i2c import i2c_bus
import rotaryio

#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.IRsensor(board.A1)
IRsensorRear = IRsensor.IRsensor(board.A0)

#instances ultrasonic sensors sides
USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D4)

wheelR = motordriver.MD13S(board.D9,board.D8)
wheelL = motordriver.MD13S(board.A15, board.A14)

def readSerial():
     if (supervisor.runtime.serial_bytes_available):
        value = input().strip()
        value = value.strip('][').split(', ')
        
        if value == "":
            pass
        elif 'motor' in value[0]:
            value.pop(0)
            value = [float(i) for i in value]
            wheelL.speed_control(int(value[0]))
            wheelL.direction_control(int(value[1]))
            wheelR.speed_control(int(value[2]))
            wheelR.direction_control(int(value[3]))
                      
sonar1 = 0
sonar2 = 0
while True:
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
        
    readSerial()
    print('send', ir_back, ir_front, sonar1, sonar2)

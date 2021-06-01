import time
import board 
import math 
import IRsensor
import adafruit_hcsr04

#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.get_distance_IR(board.A14)
IRsensorRear = IRsensor.get_distance_IR(board.A15)

#instances ultrasonic sensors sides
USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D34, echo_pin=board.D35)
USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D32, echo_pin=board.D33)
USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.D30, echo_pin=board.D31)
USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.D28, echo_pin=board.D29)



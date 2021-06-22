import time
import board
import IRsensor
import adafruit_hcsr04
import motordriver
from pwmio import PWMOut
import LED

# LED strip
LEDstatus = LED.LEDstatus

#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.IRsensor(board.A14)
IRsensorRear = IRsensor.IRsensor(board.A15)

#instances ultrasonic sensors sides
USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)
USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D8)
USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.D30, echo_pin=board.D31)
USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.D28, echo_pin=board.D29)

try:
    print(1, USsensorFL.distance)
except RuntimeError:
    pass

# Fans
FanPWM = PWMOut(pin = board.D3, frequency=5000, duty_cycle=0)


# Statemachine 
state = 1 

# Ready state
if state == 1:
    LEDstatus.blink_slow_blue()
    state = 2

# Running state
elif state == 2:
    LEDstatus.green()
    state = 3

# Battery low state 
elif state == 3:
    LEDstatus.red()
    state = 4

# Charging State
elif state == 4:
    LEDstatus.blink_red_blue()
    state = 5

# Safety State
elif state == 5:
    LEDstatus.blink_fast_red()

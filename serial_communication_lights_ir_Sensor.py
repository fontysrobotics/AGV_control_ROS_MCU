import supervisor
import time
import board
import math
import neopixel
from analogio import AnalogIn

analog_in = AnalogIn(board.A14)
pixel_pin = board.NEOPIXEL
pixels = neopixel.NeoPixel(pixel_pin, 1, brightness=0.3, auto_write=False)
color = 'green'

def get_distance_IR(pin):
    voltage = (pin.value/65535)*3.3
    distance = 5.18 * math.pow(voltage, -1.27)
    print(distance)
    
def readSerial():
     if (supervisor.runtime.serial_bytes_available):
        value = input().strip()
        value = float(value)
        if value == "":
            pass

        if value == 5.0:
            pixels.fill((0, 255, 0))
            
        if value == 6.0:
            pixels.fill((180, 0, 255))
            
        pixels.show()

while True:
    readSerial()
    get_distance_IR(analog_in)
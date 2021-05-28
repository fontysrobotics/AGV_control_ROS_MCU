import time
import board
import math
from analogio import AnalogIn
analog_in = AnalogIn(board.A14)

def get_distance_IR(pin):
    voltage = (pin.value/65535)*3.3
    distance = 5.18 * math.pow(voltage, -1.27)
    return distance

while True:
    print((get_distance_IR(analog_in),))
    time.sleep(0.1)

import math
from analogio import AnalogIn

def get_distance_IR(self, pin):
    self.pin = pin
    analog_in = AnalogIn(pin)
    voltage = (analog_in.value/65535)*3.3
    distance = 5.18 * math.pow(voltage, -1.27)
    return distance





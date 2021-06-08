import math
from analogio import AnalogIn

class IRsensor:

    def __init__(self, analog_pin):
        self._analogPin = AnalogIn(analog_pin)

    def get_distance_IR(self):
        voltage = (self._analogPin.value/65535)*3.3
        distance = 5.18 * math.pow(voltage, -1.27)
        return distance





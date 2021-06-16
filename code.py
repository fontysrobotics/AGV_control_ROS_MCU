import time
#import board 
import math 
#import IRsensor
#import adafruit_hcsr04
#import motordriver
#import Temperature
#import BMS
#from pwmio import PWMOut
import statemachine as agv_machine
from transitions.core import Transition
from transitions.extensions import GraphMachine as Machine

'''
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
'''

model = agv_machine
machine = Machine(model=model, states=model.agv_machine.states, transitions=model.agv_machine.transitions, 
                       show_auto_transitions=False, **model.agv_machine.extra_args, use_pygraphviz=False)

model.get_graph().draw('agv_state_diagram.png', prog='dot')

if __name__ == '__main__':
    print(model.state)


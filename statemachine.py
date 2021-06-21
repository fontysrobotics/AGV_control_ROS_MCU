# from transitions import Machine
from transitions.core import Transition
from transitions.extensions import GraphMachine as Machine
import time

class agv_machine(object):
    def __init__(self):
        pass

    def start(self):

            return False

    def timer(self):

           return False 

    def safety(self):

           return False         

    extra_args = dict(initial='STOP', title='DACS AGV statemachine',
                  show_conditions=True, show_state_attributes=True)

    states = [
        {'name': 'STOP', 'on_enter': ['stop_procedure','LED_yellow'], 'on_exit': 'StatusMessage'},
        {'name': 'START', 'on_enter': ['LED_blue','instantiate'], 'on_exit': 'StatusMessage'},
        {'name': 'RUNNING', 'on_enter': ['LED_green', 'driving'], 'on_exit': 'StatusMessage'},
        {'name': 'SAFE', 'on_enter': ['LED_blinkFastRed','safety_procedure'], 'on_exit': 'StatusMessage'},
        {'name': 'BATTERYLOW', 'on_enter': ['LED_red','lowpower_mode'], 'on_exit': 'StatusMessage'}
        ]

    transitions = [
        {'trigger': 'start', 'source': 'STOP', 'dest': 'START',
        'conditions':'iStart'},
        {'trigger': 'initdelay', 'source': 'START', 'dest': 'RUNNING',
        'conditions':'timer'},
        {'trigger': 'hazard', 'source': 'RUNNING', 'dest': 'SAFE',
        'conditions':'safety'},
        {'trigger': 'batterylow', 'source': 'RUNNING', 'dest': 'BATTERYLOW',
        'conditions':'batterylevel'},
        {'trigger': 'charging', 'source': 'BATTERYLOW', 'dest': 'STOP',
        'conditions':'charging'},
        {'trigger': 'stop', 'source': 'RUNNING', 'dest': 'STOP',
        'conditions':'iStop'},
        {'trigger': 'safedelay', 'source': 'SAFE', 'dest': 'STOP',
        'conditions':'timer'},
        ]

    



    

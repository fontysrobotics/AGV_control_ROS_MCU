# from transitions import Machine
from transitions.core import Transition
from transitions.extensions import GraphMachine as Machine
import time

class agv_machine(object):
    def __init__(self):
        pass

    def start(self):
        time.sleep(5)
        value = 0.4
        print(value)  
        if value > 0.3:
            return True
        else:
            return False

    def timer(self):
        time.sleep(5)
        value = 0.6
        print(value)
       
        if value > 0.5:
            return True
        else:
           return False 

    def safety(self):
        time.sleep(5)
        value = 0.6
        print(value) 
       
        if value > 0.5:
            return True
        else:
           return False         

    extra_args = dict(initial='STOP', title='DACS AGV statemachine',
                  show_conditions=True, show_state_attributes=True)

    states = [
        {'name': 'STOP', 'on_enter': ['stop_procedure','LED_yellow'], 'on_exit': 'StatusMessage'},
        {'name': 'START', 'on_enter': ['LED_blue','instantiate'], 'on_exit': 'StatusMessage'},
        {'name': 'RUNNING', 'on_enter': ['LED_green', 'driving'], 'on_exit': 'StatusMessage'},
        {'name': 'SAFE', 'on_enter': ['LED_blinkFastRed''safety_procedure'], 'on_exit': 'StatusMessage'},
        {'name': 'BATTERYLOW', 'on_enter': ['LED_red','lowpower_mode'], 'on_exit': 'StatusMessage'}
        ]

    transitions = [
        {'trigger': 'starting', 'source': 'STOP', 'dest': 'START',
        'conditions':'start'},
        {'trigger': 'init', 'source': 'START', 'dest': 'RUNNING',
        'conditions':'timer'},
        {'trigger': 'hazard', 'source': 'RUNNING', 'dest': 'SAFE',
        'conditions':'safety'},
        ]

    

model = agv_machine()
machine = Machine(model=model, states=agv_machine.states, transitions=agv_machine.transitions, 
                       show_auto_transitions=False, **agv_machine.extra_args, use_pygraphviz=False)

model.get_graph().draw('agv_state_diagram.png', prog='dot')

if __name__ == '__main__':
    agv_machine = agv_machine()
    print(model.state)

    

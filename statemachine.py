# from transitions import Machine
from transitions.extensions import GraphMachine as Machine
import time

class agv_machine(object):
    states = ['STOP' , 'START' , 'RUNNING' , 'SAFE' ]

    def __init__(self):
        self.machine = Machine(model=self, states=agv_machine.states, initial='STOP' , show_conditions=True , show_auto_transitions=False)

        self.machine.add_transition(trigger='start' , source='STOP', dest='START' , conditions=['init'], after='next_state')
        self.machine.add_transition(trigger='start', source='START', dest='RUNNING' , conditions=['user_start'],  after='next_state') #safe to desinfect
        self.machine.add_transition(trigger='start' , source='RUNNING' , dest='SAFE', conditions=['hazard'], after='next_state')
        self.machine.add_transition(trigger='start', source='SAFE', dest='STOP', conditions=['hazard_approved'], after='next_state')


    def next_state(self):
        #self.machine.next_state()
        agv_machine.trigger('start')

    def user_start(self):
        time.sleep(5)
        value = 0.4
        print(value)
        print(0,agv_machine.state)  
        if value > 0.3:
            return True
        else:
            return False

    def hazard(self):
        time.sleep(5)
        value = 0.6
        print(value)
        print(1,agv_machine.state)  
       
        if value > 0.5:
            return True
        else:
           return False 

    def hazard_approved(self):
        time.sleep(5)
        value = 0.6
        print(value)
        print(2,agv_machine.state)  
       
        if value > 0.5:
            return True
        else:
           return False         


model = agv_machine()
model.get_graph().draw('my_state_diagram.png', prog='dot')

if __name__ == '__main__':
    agv_machine = agv_machine()
    print(1,agv_machine.state)
    agv_machine.trigger('start')
    print(5,agv_machine.state)
    

# from transitions import Machine
from transitions.extensions import GraphMachine as Machine
import time

class agv_machine (object):
    states = ['stop' , 'start' , 'running' , 'safe' ]

    def __init__(self):
        self.machine = Machine(model=self, states=agv_machine.states, initial='idle' , show_conditions=True , show_auto_transitions=False)

        self.machine.add_transition(trigger='start' , source='idle', dest='scan_objects' , conditions=['green_button'], after='next_state')
        self.machine.add_transition(trigger='start', source='scan_objects', dest='desinfecting' , conditions=['safe_to_desinfect'],  after='next_state') #safe to desinfect
        self.machine.add_transition(trigger='start' , source='scan_objects' , dest='not_safe', conditions=['not_safe_to_desinfect'], after='next_state')
        self.machine.add_transition(trigger='start', source='desinfecting', dest='pause', conditions=['orange_button'], after='next_state')


    def next_state(self):
        #self.machine.next_state()
        agv_machine.trigger('start')

    def green_button(self):
        time.sleep(5)
        value = 0.4
        print(value)
        print(2,agv_machine.state)  
        if value > 0.3:
            return True
        else:
            return False

    def orange_button(self):
        time.sleep(5)
        value = 0.6
        print(value)
        print(4,agv_machine.state)  
       
        if value > 0.5:
            return True
        else:
           return False 

    def red_button(self):
        time.sleep(5)
        value = 0.6
        print(value)
        print(4,agv_machine.state)  
       
        if value > 0.5:
            return True
        else:
           return False         


    def safe_to_desinfect(self):
        time.sleep(5)
        value = 0.5
        print(value)
        print(3,agv_machine.state)  
       
        if value > 0.3:
            return True
        else:
            return False    

    def not_safe_to_desinfect(self):
        time.sleep(5)
        value = 0.5
        print(value)
        print(3,agv_machine.state)  

    def reedswitch(self):
        time.sleep(5)
        value = 0.5
        print(value)
        print(3,agv_machine.state)  
       
        if value > 0.3:
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
    

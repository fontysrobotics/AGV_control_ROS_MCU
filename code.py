from rotaryio import IncrementalEncoder
from pwmio import PWMOut
from time import monotonic, sleep
import board

class Driver(object):
    def __init__(self):
        self.enc = IncrementalEncoder(board.GP18, board.GP19)
        self.pwm_A = PWMOut(board.GP12, duty_cycle=0, frequency=1000)
        self.pwm_B = PWMOut(board.GP13, duty_cycle=0, frequency=1000)
        self.pwm_A.duty_cycle = 0x0000 #FFFF is the higest and 0000 no velocity
    def spin(self):
        stamp = monotonic() #timestamp use to calculate the delta
        sleep(1) #No idea if needed, actually not needed.
        last_pose = 0

        while(True):
            delta = (monotonic() - stamp)
            stamp = monotonic()
            current_pose = self.enc.position #number of pulses
            vel = (current_pose - last_pose) / delta
            last_pose = current_pose
            print("Velocity mm/s: " + str(vel * 1.396263402))#(2pi * r)/pulses per rotation (measured by hand with tape)
            sleep(0.1)

if __name__ == '__main__':
    drv = Driver()
    drv.spin()
    
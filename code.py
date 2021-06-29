import time
import board
import IRsensor
import adafruit_hcsr04
import motordriver
from pwmio import PWMOut
import LED
import BMS


class Statemachine:

    # BMS
    charging = BMS.charging
    BatteryLevel = BMS.BateryLevel

    # Emergency Stop
    emergencyStop = board.D40

    # LED strip
    LEDstatus = LED.LEDstatus

    #instances Infrared distance sensors Front and rear
    IRsensorFront = IRsensor.IRsensor(board.A14)
    IRsensorRear = IRsensor.IRsensor(board.A15)

    #instances ultrasonic sensors sides
    USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)
    USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D8)
    USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.D30, echo_pin=board.D31)
    USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.D28, echo_pin=board.D29)

    # Communication Vars
    Start = communication.start
    Stop = Communication.stop
    Status = Communication.status

    # Fans
    FanPWM = PWMOut(pin = board.D3, frequency=5000, duty_cycle=0)

    def __init__(self):
        state = 1 
        #statusmessage to master

    def safety_procedure(self):
        pass

    def recieve_data(self):
        pass

    def transmit_data(self):
        pass

    def handle_data():
        pass

    def state_flow(self):
        # Ready state
        if self.state == 1:
            self.LEDstatus.blink_slow_blue()
            print('waiting for user input')

            if self.Start:
                #statusmessage to master
                self.state = 2

            elif self.emergencyStop:
                #statusmessage to master
                self.state = 5

            elif self.charging:
                #statusmessage to master
                self.state = 4
        

        # Running state
        elif self.state == 2:
            self.LEDstatus.green()
            #recieve Data

            if self.Stop:
                #statusmessage to master
                self.state = 1

            elif self.emergencyStop or self.Tbat > self.TbatMax or Fdist < MaxDist or Rdist < MaxDist:
                #statusmessage to master
                self.state = 5

            elif self.charging:
                #statusmessage to master
                self.state = 4

            elif self.BatteryLevel < 5:
                #statusmessage to master
                self.state = 3

        # Battery low state 
        elif self.state == 3:
            self.LEDstatus.red()

            if self.charging:
                #statusmessage to master
                self.state = 4

            elif self.BatteryLevel < 5:
                #statusmessage to master
                self.state = 3


        # Charging State
        elif self.state == 4:
            self.LEDstatus.blink_red_blue()

            #statusmessage to master
            if self.BatteryLevel 
            self.statemachinestate = 5

        # Safety State
        elif self.state == 5:
            LEDstatus.blink_fast_red()
            self.safety_procedure()

        print('state', self.state)    
        return self.state



def main(args=None): 
    Statemachine.state_flow()





if __name__ == '__main__':
    main()
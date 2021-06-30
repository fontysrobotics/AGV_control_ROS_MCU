from Sensoren_sender import IRsensorFront, IRsensorRear
import time
import board
import IRsensor
import adafruit_hcsr04
import adafruit_mcp9808
import adafruit_ina260
import motordriver
from pwmio import PWMOut
import LED
import BMS
import communication


class Statemachine:

    # Emergency Stop
    emergencyStop = board.D40

    # LED strip
    LEDstatus = LED.LEDstatus

    # Motor drivers
    rightMotor = motordriver.MD13S(PWM_pin=board.D8, dir_pin=board.D9, enc_pinA=board.D6, enc_pin_B=board.D7)
    leftMotor = motordriver.MD13S(PWM_pin=board.A9, dir_pin=board.A8, enc_pinA=board.A10, enc_pin_B=board.A11)

    #instances Infrared distance sensors Front and rear
    IRsensorF = IRsensor.IRsensor(board.A14)
    IRsensorR = IRsensor.IRsensor(board.A15)

    #instances ultrasonic sensors sides
    USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D5)
    USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
    USsensorRR = adafruit_hcsr04.HCSR04(trigger_pin=board.A14, echo_pin=board.A15)
    USsensorRL = adafruit_hcsr04.HCSR04(trigger_pin=board.A12, echo_pin=board.A13)

    # Communication Vars
    serial = communication.serial()
    Tsensor1 = communication.i2c()
    Tsensor2 = communication.i2c()
    Vsensor = communication.i2c()

    # Temperature sensors
    TbatF = adafruit_mcp9808.MCP9808(Tsensor1.i2c, Tsensor1.adress)
    TbatR = adafruit_mcp9808.MCP9808(Tsensor2.i2c, Tsensor2.adress)

    # BMS
    BMS = adafruit_ina260.INA260(Vsensor.i2c, Vsensor.adress)
    BatteryLevel = (BMS.voltage-11)/5.8*100
    charging = DigitalInOut(board.D39)
    charging.direction = Direction.INPUT

    # Fans
    FanPWM = PWMOut(pin = board.D31, frequency=5000, duty_cycle=0)

    def __init__(self):
        state = 1 

    def safety_procedure(self):
        self.leftMotor._pwm = 0
        self.rightMotor._pwm = 0

    def safety_check(self):
        return True

    def handle_data(self):
        oData = [] 
        oData[0] = self.leftMotor.get_motor_speed()
        oData[1] = self.rightMotor.get_motor_speed()
        oData[2] = self.USsensorFL
        oData[3] = self.USsensorFR
        oData[4] = self.USsensorRL
        oData[5] = self.USsensorRR
        oData[6] = self.IRsensorF
        oData[7] = self.IRsensorR

    def state_flow(self):
        # Ready state
        if self.state == 1:

            self.LEDstatus.blink_slow_blue()
            print('waiting for user input')

            if self.serial.userInput == "start":
                self.state = 2
                self.serial.status_message(self.state) # Status message to master
                
            elif self.emergencyStop:
                self.state = 5
                self.serial.status_message(self.state) # Status message to master
                
            elif self.charging.value:
                self.state = 4
                self.serial.status_message(self.state) # Status message to master
        

        # Running state
        elif self.state == 2:
            self.LEDstatus.green()
            communication.serial.read_data()
            self.handle_data()
 
            if self.serial.userInput == "stop":
                self.state = 1
                self.serial.status_message(self.state) # Status message to master

            elif self.emergencyStop or self.TbatF.temperature>60 or self.TbatR.temperature>60 or IRsensorFront.get_distance_IR()<5 or IRsensorRear.get_distance_IR()<5:
                self.state = 5
                self.serial.status_message(self.state) # Status message to master
                
            elif self.charging.value:
                self.state = 4
                self.serial.status_message(self.state) # Status message to master
                

            elif self.BatteryLevel < 5:
                self.state = 3
                self.serial.status_message(self.state) # Status message to master

        # Battery low state 
        elif self.state == 3:
            self.LEDstatus.red()

            if self.charging.value:
                self.state = 4
                self.serial.status_message(self.state) # Status message to master

            elif self.BatteryLevel>20 and not self.charging.value:
                self.state = 3
                self.serial.status_message(self.state) # Status message to master
            
            elif self.emergencyStop or self.TbatF.temperature>60 or self.TbatR.temperature>60 or IRsensorFront.get_distance_IR()<5 or IRsensorRear.get_distance_IR()<5:
                self.state = 5
                self.serial.status_message(self.state) # Status message to master


        # Charging State
        elif self.state == 4:
            self.LEDstatus.blink_red_blue()

            if self.BatteryLevel<20 and not self.charging.value:
                self.state = 3
                self.serial.status_message(self.state) # Status message to master

            elif self.BatteryLevel>20 and not self.charging.value:
                self.state = 1
                self.serial.status_message(self.state) # Status message to master

            elif self.emergencyStop or self.TbatF.temperature>60 or self.TbatR.temperature>60 or IRsensorFront.get_distance_IR()<5 or IRsensorRear.get_distance_IR()<5:
                self.state = 5
                self.serial.status_message(self.state) # Status message to master

        # Safety State
        elif self.state == 5:
            self.LEDstatus.blink_fast_red()
            self.safety_procedure()

            if self.safety_check():
                state = 1


        print('state: ', self.state)    
        return self.state



def main(args=None): 
    Statemachine.state_flow()



if __name__ == '__main__':
    main()
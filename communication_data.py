import board
import IRsensor
import adafruit_hcsr04
import motordriver
import supervisor
import LED
import encoder

#instances Infrared distance sensors Front and rear
IRsensorFront = IRsensor.IRsensor(board.A1)
IRsensorRear = IRsensor.IRsensor(board.A0)

#instances ultrasonic sensors sides
USsensorFR = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
USsensorFL = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D4)

wheelR = motordriver.MD13S(board.D9,board.D8)
wheelL = motordriver.MD13S(board.A15, board.A14)

encL = encoder.motor_enc(board.D10, board.D11)
encR = encoder.motor_enc(board.D8, board.D9)
odom = encoder.odom_calc()

led = LED.LEDstatus(board.D1)

def readSerial():
     if (supervisor.runtime.serial_bytes_available):
        value = input().strip()
        value = value.strip('][').split(', ')
        
        if value == "":
            pass
        elif 'motor' in value[0]:
            value.pop(0)
            value = [float(i) for i in value]
            wheelL.speed_control(int(value[0]))
            wheelL.direction_control(int(value[1]))
            wheelR.speed_control(int(value[2]))
            wheelR.direction_control(int(value[3]))

        elif 'task' in value[0]:
            value.pop(0)
            value = [float(i) for i in value]
            value = value[0]
            if value == -4: 
                led.purple()
            elif value == -3: 
                led.blue()
            elif value == -2: 
                led.green()
            elif value == -1:
                led.blink_fast_red()
            elif value == 0:
                led.white()
            elif value >= 1:
                led.blink_slow_blue()
                  
sonar1 = 0
sonar2 = 0
led.clear()

while True:
    ir_back = IRsensorRear.get_distance_IR()
    ir_front = IRsensorFront.get_distance_IR()
    try:
        sonar1 = USsensorFR.distance/100
    except RuntimeError:
        sonar1 = sonar1/100
    try:
        sonar2 = USsensorFL.distance/100
    except RuntimeError:
        sonar2 = sonar2/100
        
    count_1 = encL.get_motor_speed()
    count_2 = encR.get_motor_speed()
    delta_vel_center, delta_ang_center = odom.Odometry(count_1, count_2)

    readSerial()
    print('send', ir_back, ir_front, sonar1, sonar2, delta_vel_center, delta_ang_center)
import supervisor
import adafruit_mpc9808
import board


class serial:
    def __init__(self, o_data, status):
        self.DATA = ""
        self.userInput = ""
        self.oDATA = o_data
        self.Status = status

    def write_data(self):
        print(self.oDATA)

        
    def read_data(self):
        if (supervisor.runtime.serial_bytes_available):
            value = input().strip()
            value = float(value)
            if value == "":
                pass
            else:
                self.DATA = value

    def user_input(self):
        if (supervisor.runtime.serial_bytes_available):
            iUser = input().strip()
            iUser = str(iUser)
            if iUser == "":
                pass
            elif iUser == "start":
                self.userInput = "start"
            
            elif iUser == "stop":
                self.userInput = "stop"

            else:
                self.userInput = "error"

    def status_message(self):
        print(self.Status)


class i2c():
    def __init__(self):
        self.i2c = board.I2C()
       
        while not self.i2c.try_lock():
            pass   
        
        self.adress = [hex(device_address) for device_address in self.i2c.scan()]

    def return_adress(self):
        return self.adress

    def exit(self):
        self.i2c.unlock()


   

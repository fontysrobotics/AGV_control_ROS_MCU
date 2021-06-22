import time
import board
import adafruit_mcp9808


class i2c_bus():
    def __init__(self):
        self.i2c = board.I2C()

        self.mcp_1 = adafruit_mcp9808.MCP9808(self.i2c, 0x19)
        self.mcp_2 = adafruit_mcp9808.MCP9808(self.i2c, 0x18)
        self.temperature = [self.mcp_1.temperature, self.mcp_2.temperature]
       

        while not self.i2c.try_lock():
            pass   
        
        self.adress = [hex(device_address) for device_address in self.i2c.scan()]

    def return_temperature(self):
        return self.temperature

    def return_adress(self):
        return self.adress

    def exit(self):
        self.i2c.unlock()

if __name__ == '__main__':
    i2c = i2c_bus()
    print(i2c.read_temperature())
    i2c.exit()
import adafruit_mcp9808
import board

i2c = board.I2C()

# Lock the I2C device before we try to scan
while not i2c.try_lock():
    pass
# Print the addresses found once
print("I2C addresses found:", [hex(device_address)
                               for device_address in i2c.scan()])

# Unlock I2C now that we're done scanning.
i2c.unlock()

# Create library object on our I2C port
sensor = adafruit_mcp9808.MCP9808(i2c)





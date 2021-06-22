import board
import time 
import neopixel

class LEDstatus:  
    PIXEL_PIN = board.D1  # pin that the NeoPixel is connected to
    ORDER = neopixel.RGB  # pixel color channel order
    RED = (100, 50, 150)  # color to blink
    BLUE = (0, 0, 0)
    GREEN = (0, 0, 0)
    CLEAR = (0, 0, 0) 
    
    def __init__(self):
        pixel = neopixel.NeoPixel(self.PIXEL_PIN, 1, pixel_order=self.ORDER) # Create the NeoPixel object
        self.initialOnTime = time.monotonic()
        self.initialOffTime = time.monotonic()

    def blink_fast_red(self):
        currentTime = time.monotonic()
        delayOn = 0.5
        delayOff = 0.25
        if (currentTime-self.initialOnTime)>delayOn:
            self.pixel[0] = self.RED
            self.initialOffTime = time.monotonic()
        else:
            self.pixel[0] = self.CLEAR
            if (currentTime-self.initialOffTime)>delayOff:
                self.initialOnTime = time.monotonic()

    def green(self):
        self.pixel[0] = self.GREEN

    def red(self):
        self.pixel[0] = self.RED

    def blink_slow_blue(self):
        currentTime = time.monotonic()
        delayOn = 2.0
        delayOff = 1.0
        if (currentTime-self.initialOnTime)>delayOn:
            self.pixel[0] = self.BLUE
            self.initialOffTime = time.monotonic()
        else:
            self.pixel[0] = self.CLEAR
            if (currentTime-self.initialOffTime)>delayOff:
                self.initialOnTime = time.monotonic()

    def blink_red_blue(self):
        currentTime = time.monotonic()
        delay = 1.0
        if (currentTime-self.initialOnTime)>delay:
            self.pixel[0] = self.RED
            self.initialOffTime = time.monotonic()
        else:
            self.pixel[0] = self.BLUE
            if (currentTime-self.initialOffTime)>delay:
                self.initialOnTime = time.monotonic()

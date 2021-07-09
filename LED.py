import board
import time 
import neopixel

class LEDstatus:  
    ORDER = neopixel.RGB  # pixel color channel order
    RED = (255, 0, 0)  # color to blink
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    CLEAR = (0, 0, 0) 
    PURPLE = (180, 0, 255)
    WHITE = (200,200,200)
    
    def __init__(self, led_pin):
        PIXEL_PIN = led_pin
        self.pixel = neopixel.NeoPixel(self.PIXEL_PIN, 1, pixel_order=self.ORDER) # Create the NeoPixel object
        self.initialOnTime = time.monotonic()
        self.initialOffTime = time.monotonic()

    def blink_fast_red(self):
        currentTime = time.monotonic()
        delayOn = 0.5
        delayOff = 0.25
        if (currentTime-self.initialOnTime)>delayOn:
            self.pixel.fill(self.RED)
            self.initialOffTime = time.monotonic()
        else:
            self.pixel(self.CLEAR)
            if (currentTime-self.initialOffTime)>delayOff:
                self.initialOnTime = time.monotonic()

    def white(self):
        self.pixel.fill(self.WHITE)

    def purple(self):
        self.pixel.fill(self.PURPLE)

    def blue(self):
        self.pixel.fill(self.BLUE)

    def green(self):
        self.pixel.fill(self.GREEN)

    def red(self):
        self.pixel.fill(self.RED)

    def blink_slow_blue(self):
        currentTime = time.monotonic()
        delayOn = 2.0
        delayOff = 1.0
        if (currentTime-self.initialOnTime)>delayOn:
            self.pixel.fill(self.BLUE)
            self.initialOffTime = time.monotonic()
        else:
            self.pixel(self.CLEAR)
            if (currentTime-self.initialOffTime)>delayOff:
                self.initialOnTime = time.monotonic()

    def blink_red_blue(self):
        currentTime = time.monotonic()
        delay = 1.0
        if (currentTime-self.initialOnTime)>delay:
            self.pixel.fill(self.RED)
            self.initialOffTime = time.monotonic()
        else:
            self.pixel(self.BLUE)
            if (currentTime-self.initialOffTime)>delay:
                self.initialOnTime = time.monotonic()

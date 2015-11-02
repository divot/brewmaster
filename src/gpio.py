import RPi.GPIO as GPIO
from smbus import SMBus

class StandardGPIO(object):

    GPIO.setmode(GPIO.BOARD)

    def __init__(self, port, default=False, inverted=False):
        self.port = port
        if inverted:
            self.on = GPIO.LOW
            self.off = GPIO.HIGH
        else:
            self.on = GPIO.HIGH
            self.off = GPIO.LOW
        GPIO.setup(self.port, GPIO.OUT)
        if default:
            self.on()
        else:
            self.off()

    def __del__(self):
        GPIO.cleanup(self.port)

    def on(self):
        GPIO.output(self.port, self.on)

    def off(self):
        GPIO.output(self.port, self.off)

class PCF8574(object):

    class GPIO(object):

        def __init__(self, expander, bit, inverted=False):
            self.expander = expander
            self.bit = bit
            self.inverted = inverted

        def on(self):
            self.expander.write_bit(self.bit, not self.inverted)

        def off(self):
            self.expander.write_bit(self.bit, self.inverted)
    
    def __init__(self, address, bus=1, byte=0):
        self.address = address
        self.bus = SMBus(bus)
        self.byte = byte
        self.data = 0xFF

    def __del__(self):
        self.write_byte(0xFF)

    def commit(self):
        self.bus.write_byte_data(self.address, self.byte, self.data)
        
    def write_byte(self, data):
        self.data = data
        self.commit()

    def write_bit(self, bit, value):
        mask = 1 << bit
        if value:
            self.data |= mask
        else:
            self.data &= ~mask
        self.commit()

    def get_gpio(self, bit, inverted=False):
        return self.GPIO(self, bit, inverted)

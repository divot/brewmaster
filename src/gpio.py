import RPi.GPIO
from smbus import SMBus

class StandardGPIO(object):

    GPIO.setmode(GPIO.BOARD)

    def __init__(self, port):
        self.port = port
        GPIO.setup(self.port, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup(self.port)

    def on(self):
        GPIO.output(self.port, GPIO.HIGH)

    def off(self):
        GPIO.output(self.port, GPIO.LOW)

class PCF8574(object):

    class GPIO(object):

        def __init__(self, expander, bit):
            self.expander = expander
            self.bit = bit

        def on(self):
            self.expander.set_bit(self.bit)

        def off(self):
            self.expander.clear_bit(self.bit)
    
    def __init__(self, address, bus=1, byte=0):
        self.address = address
        self.bus = SMBus(bus)
        self.byte = byte
        self.data = 0xFF

    def write(self):
        self.bus.write_byte_data(self.address, self.byte, self.data)
        
    def write_data(self, data):
        self.data = data
        self.write()

    def set_bit(self, bit):
        mask = 1 << bit
        print self.data
        print self.data & mask
        if (self.data & mask == 0):
            self.data += mask
            print self.data
            self.write()

    def clear_bit(self, bit):
        mask = 1 << bit
        print self.data
        print self.data & mask
        if (self.data & mask != 0):
            self.data -= mask
            print self.data
            self.write()

    def get_gpio(self, bit):
        return self.GPIO(self, bit)

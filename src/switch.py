import abc
import RPi.GPIO as GPIO

class Switch(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, devices = None):
        self.devices = devices

    def get_devices(self):
        return devices

    @abc.abstractmethod
    def switch_on(self):
        pass

    @abc.abstractmethod
    def switch_on(self):
        pass

class GPIOSwitch(Switch):

    GPIO.setmode(GPIO.BCM)

    def __init__(self, port, devices = None):
        super(GPIOSwitch, self).__init__(devices)
        self.port = port
        GPIO.setup(self.port, GPIO.OUT)
        GPIO.output(self.port, GPIO.LOW)

    def switch_on(self):
        GPIO.output(self.port, GPIO.HIGH)

    def switch_off(self):
        GPIO.output(self.port, GPIO.LOW)

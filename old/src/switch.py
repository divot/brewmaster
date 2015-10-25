import abc
import RPi.GPIO as GPIO
import component
import threading

class Switch(component.ComponentContainer):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.timer = None

    @abc.abstractmethod
    def switch_on(self):
        pass

    @abc.abstractmethod
    def switch_off(self):
        pass

    def timed_on(self, time):
        if self.timer:
            self.timer.cancel()
            del self.timer
        else:
            self.switch_on()
        self.timer = threading.Timer(time, self.__timer_func)
        self.timer.start()

    def timed_cancel(self):
        if self.timer:
            self.__timer_func()

    def __timer_func(self):
        self.switch_off()
        self.timer = None

class GPIOSwitch(Switch):

    GPIO.setmode(GPIO.BCM)

    def __init__(self, port):
        Switch.__init__(self)
        self.port = port
        GPIO.setup(self.port, GPIO.OUT)
        GPIO.output(self.port, GPIO.LOW)

    def switch_on(self):
        GPIO.output(self.port, GPIO.HIGH)

    def switch_off(self):
        GPIO.output(self.port, GPIO.LOW)

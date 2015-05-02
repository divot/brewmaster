import abc
import component
import switch

class Valve(component.ComponentContainer):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

class ThreeWireValve(Valve):

    def __init__(self, open_port, close_port, time=5.0):
        self.open_switch = switch.GPIOSwitch(open_port)
        self.close_switch = switch.GPIOSwitch(close_port)
        self.time = time

    def open(self):
        self.close_switch.timed_cancel()
        self.open_switch.timed_on(self.time)

    def close(self):
        self.open_switch.timed_cancel()
        self.close_switch.timed_on(self.time)


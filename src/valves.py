from liquidcomponent import LiquidComponent
import RPi.GPIO as GPIO
import threading

class TwoWayValve(LiquidComponent):

    DEFAULT_NAME = "TwoWayValve"
    DEFAULT_PORTS = ["Port1", "Port2"]
    STATE_CLOSED = "Closed"
    STATE_OPEN = "Open"
    STATES = [STATE_CLOSED, STATE_OPEN]

    def __init__(self,
                 name=DEFAULT_NAME,
                 ports=DEFAULT_PORTS):
        super(TwoWayValve, self).__init__(name, ports, self.STATES)
        self.ports[ports[0]].add_path(self.ports[ports[1]], TwoWayValve.STATE_OPEN)
        self.ports[ports[1]].add_path(self.ports[ports[0]], TwoWayValve.STATE_OPEN)

class ThreeWayValve(LiquidComponent):

    DEFAULT_NAME = "ThreeWayValve"
    DEFAULT_PORTS = ["CommonPort", "Port1", "Port2"]
    STATES = ["Position0", "Position1"]
    STATE_POSITION_0 = STATES[0]
    STATE_POSITION_1 = STATES[1]

    def __init__(self,
                 name=DEFAULT_NAME,
                 ports=DEFAULT_PORTS):
        super(ThreeWayValve, self).__init__(name,
                                            ports,
                                            self.STATES)
        self.ports[ports[0]].add_path(self.ports[ports[1]], ThreeWayValve.STATE_POSITION_0)
        self.ports[ports[1]].add_path(self.ports[ports[0]], ThreeWayValve.STATE_POSITION_0)
        self.ports[ports[0]].add_path(self.ports[ports[2]], ThreeWayValve.STATE_POSITION_1)
        self.ports[ports[2]].add_path(self.ports[ports[0]], ThreeWayValve.STATE_POSITION_1)

class TwoWayValveMISOLTwoWire(TwoWayValve):

    def __init__(self,
                 openio,
                 closeio,
                 name=TwoWayValve.DEFAULT_NAME,
                 ports=TwoWayValve.DEFAULT_PORTS):
        super(TwoWayValveMISOLTwoWire, self).__init__(name, ports)
        self.openio = openio
        self.closeio = closeio
        GPIO.setup(openio, GPIO.OUT)
        GPIO.setup(closeio, GPIO.OUT)
        self.close()

    def __del__(self):
        GPIO.setup(openio, )
        GPIO.setup(closeio, )

    def set_state(self, state):
        super(TwoWayValveMISOLTwoWire, self).set_state(state)
        if state == "Closed":
            self.close()
        elif state == "Open":
            self.open()

    def open(self):
        GPIO.output(self.closeio, GPIO.LOW)
        GPIO.output(self.openio, GPIO.HIGH)

    def close(self):
        GPIO.output(self.openio, GPIO.LOW)
        GPIO.output(self.closeio, GPIO.HIGH)

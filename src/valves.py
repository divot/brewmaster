from liquidcomponent import LiquidComponent
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
                 closeio,
                 openio,
                 name=TwoWayValve.DEFAULT_NAME,
                 ports=TwoWayValve.DEFAULT_PORTS):
        super(TwoWayValveMISOLTwoWire, self).__init__(name, ports)
        self.openio = openio
        self.closeio = closeio
        self.close()

    def set_state(self, state):
        super(TwoWayValveMISOLTwoWire, self).set_state(state)
        if state == "Closed":
            self.close()
        elif state == "Open":
            self.open()


    def close(self):
        self.openio.off()
        self.closeio.on()

    def open(self):
        self.closeio.off()
        self.openio.on()

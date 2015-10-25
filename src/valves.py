from liquidcomponent import LiquidComponent

class TwoWayValve(LiquidComponent):

    DEFAULT_NAME = "TwoWayValve"
    DEFAULT_PORTS = ["Port1", "Port2"]
    DEFAULT_STATES = ["Closed", "Open"]

    def __init__(self,
                 name=DEFAULT_NAME,
                 ports=DEFAULT_PORTS,
                 states=DEFAULT_STATES):
        super(TwoWayValve, self).__init__(name, ports, states)
        self.ports[ports[0]].add_path(self.ports[ports[1]], self.states[1])
        self.ports[ports[1]].add_path(self.ports[ports[0]], self.states[1])

class ThreeWayValve(LiquidComponent):

    DEFAULT_NAME = "ThreeWayValve"
    DEFAULT_PORTS = ["CommonPort", "Port1", "Port2"]
    DEFAULT_STATES = ["Port1", "Port2"]

    def __init__(self,
                 name=DEFAULT_NAME,
                 ports=DEFAULT_PORTS,
                 states=DEFAULT_STATES):
        super(ThreeWayValve, self).__init__(name, ports, states)
        self.ports[ports[0]].add_path(self.ports[ports[1]], self.states[0])
        self.ports[ports[1]].add_path(self.ports[ports[0]], self.states[0])
        self.ports[ports[0]].add_path(self.ports[ports[2]], self.states[1])
        self.ports[ports[2]].add_path(self.ports[ports[0]], self.states[1])

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

    DEFAULT_ACTION_TIME = 4

    def __init__(self,
                 closeio,
                 openio,
                 action_time=DEFAULT_ACTION_TIME,
                 name=TwoWayValve.DEFAULT_NAME,
                 ports=TwoWayValve.DEFAULT_PORTS):
        super(TwoWayValveMISOLTwoWire, self).__init__(name, ports)
        self.openio = openio
        self.closeio = closeio
        self.action_time = action_time
        self.timer = None
        self.close()

    def set_state(self, state):
        if state == STATE_CLOSED:
            self.close()
        elif state == STATE_OPEN:
            self.open()

    def wait_for_state(self):
        if self.timer:
            self.timer.join()

    def close(self):
        self.openio.off()
        self.closeio.on()
        self._change_state("Closed")

    def open(self):
        self.closeio.off()
        self.openio.on()
        self._change_state("Open")

    def _change_state(self, state):
        if self.timer:
            self.timer.cancel()
            del self.timer

        self.state_valid = False
        self.state = state

        self.timer = threading.Timer(
            self.action_time,
            self._revalidate_state
        )
        self.timer.start()

    def _revalidate_state(self):
        self.state_valid = True
        self.openio.off()
        self.closeio.off()

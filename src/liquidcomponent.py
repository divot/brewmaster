
class LiquidPort(object):

    def __init__(self, name, parent_component, states):
        self.name = name
        self.parent_component = parent_component
        self.graph = {}
        for state in states:
            self.graph[state] = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_path(self, port, state):
        self.graph[state].append(port)

    def find_all_paths(self,
                       current_state,
                       end_component,
                       path=[],
                       internal_path=[]):

        internal_path = internal_path + [self]
        new_path = path + [ (self.parent_component, current_state, internal_path) ]

        if self.parent_component == end_component:
            return [ new_path ]

        paths = []

        for port in self.graph[current_state]:

            if port.parent_component is self.parent_component:
                if port not in internal_path:
                    foundpaths = port.find_all_paths(current_state,
                                                     end_component,
                                                     path,
                                                     internal_path)
                    for foundpath in foundpaths:
                        paths.append(foundpath)

            elif port.parent_component not in [elem[0] for elem in new_path]:
                for state in port.parent_component.states:
                    foundpaths = port.find_all_paths(state,
                                                     end_component,
                                                     new_path)
                    for foundpath in foundpaths:
                        paths.append(foundpath)


        return paths


class LiquidComponent(object):

    DEFAULT_NAME = "Component"
    DEFAULT_PORTS = [ "Port" ]
    DEFAULT_STATES = [ "Default" ]

    def __init__(self,
                 name=DEFAULT_NAME,
                 ports=DEFAULT_PORTS,
                 states=DEFAULT_STATES):
        self.name = name
        self.states = states
        self.ports = {}
        for port in ports:
            self.ports[port] = LiquidPort(port, self, states)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def find_all_paths(self, end_component):
        all_paths = []
        for state in self.states:
            for port in self.ports.values():
                all_paths += port.find_all_paths(state,
                                                 end_component)
        return all_paths

    def add_path(self, target, port=None):
        if not port:
            assert(len(self.ports) == 1)
            port = self.ports.values()[0].name

        if isinstance(target, LiquidComponent):
            assert(len(target.ports) == 1)
            target = target.ports.values()[0]

        for state in self.states:
            self.ports[port].add_path(target, state)

class Kettle(LiquidComponent):

    DEFAULT_NAME = "Kettle"

    def __init__(self, name=DEFAULT_NAME):
        super(Kettle, self).__init__(name)

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

k1 = Kettle("K1")
k2 = Kettle("K2")
k3 = Kettle("K3")
v1 = TwoWayValve()
v2 = ThreeWayValve()

k1.add_path(v1.ports["Port1"])
v1.add_path(k1, "Port1")

k2.add_path(v1.ports["Port2"])
v1.add_path(k2, "Port2")

k1.add_path(v2.ports["CommonPort"])
v2.add_path(k1, "CommonPort")

k2.add_path(v2.ports["Port1"])
v2.add_path(k2, "Port1")

k3.add_path(v2.ports["Port2"])
v2.add_path(k3, "Port2")

print "K1 -> K2"
print k1.find_all_paths(k2)
print "K2 -> K1"
print k2.find_all_paths(k1)
print
print "K1 -> K3"
print k1.find_all_paths(k3)
print "K3 -> K1"
print k3.find_all_paths(k1)
print
print "K2 -> K3"
print k2.find_all_paths(k3)
print "K3 -> K2"
print k3.find_all_paths(k2)


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
        self.state = states[0]

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

    def set_state(self, state):
        self.state = state

from numpy import matrix
from numpy import zeros
"""

Ports
- Inputport
- OutputPort
- InputOutputPort

Paths

States

"""

total_num_ports = 0
total_num_states = 1
components = set()
storagecomponents = set()

class Port(object):
    pass

class Heater(object):
    pass

class Thermometer(object):
    pass

class Component(object):

    paths = [ [ [ 1 ] ] ]

    def __init__(self, paths, volume = 0):
        global total_num_ports
        global total_num_states

        assert(len(paths) > 0)

        self.paths = []
        for path in paths:
            self.paths.append(matrix(path))

        shape = self.paths[0].shape
        assert(len(shape) == 2)
        assert(shape[0] == shape[1])

        for path in self.paths:
            assert(path.shape == shape)

        self.num_ports = shape[0]
        self.base_port_id = total_num_ports
        total_num_ports += self.num_ports
        self.num_states = len(self.paths)
        total_num_states *= self.num_states

        self.ports = [set() for _ in range(self.num_ports)]

        components.add(self)

    def connect(self, localport, remoteport, component):
        assert(self.num_ports > localport)
        assert(component.num_ports > remoteport)
        assert((component, remoteport) not in self.ports[localport])
        assert((self, localport) not in component.ports[remoteport])

        self.__connect__(localport, remoteport, component)
        component.__connect__(remoteport, localport, self)

    def disconnect(self, localport, remoteport, component):
        assert(self.num_ports > localport)
        assert(component.num_ports > remoteport)
        assert((component, remoteport) in self.ports[localport])
        assert((self, localport) in component.ports[remoteport])

        self.__disconnect__(localport, remoteport, component)
        component.__disconnect__(remoteport, localport, component)

    def __connect__(self, localport, remoteport, component):
        self.ports[localport].add((component, remoteport))

    def __disconnect__(self, localport, remoteport, component):
        self.ports[localport].remove((component, remoteport))

class StorageComponent(Component):

    def __init__(self, volume = 0, *args):
        storagecomponents.add(self)
        self.volume = volume
        super(StorageComponent, self).__init__(*args)

class BallValve2Way(Component):

    def __init__(self):
        paths = [ [ [ 1, 0 ],
                    [ 0, 1 ] ],
                  [ [ 1, 1 ],
                    [ 1, 1 ] ] ]
        super(BallValve2Way, self).__init__(paths)

class BallValve3Way(Component):

    def __init__(self):
        paths = [ [ [ 1, 0, 1 ],
                    [ 0, 1, 0 ],
                    [ 1, 0, 1 ] ],
                  [ [ 1, 1, 0 ],
                    [ 1, 1, 0 ],
                    [ 0, 0, 1 ] ] ]
        super(BallValve3Way, self).__init__(paths)

class Pump(Component):

#    ports
    num_ports = 2
    closed_paths = [ ]
    open_paths = [ (0, 1) ]
#    heaters
#    states
    states = [ (closed_paths, open_paths) ]

    def __init__(self):
        paths = [ [ [ 1, 0 ],
                    [ 0, 1 ] ],
                  [ [ 1, 1 ],
                    [ 0, 1 ] ] ]
        super(Pump, self).__init__(paths)

class Kettle(StorageComponent):

    def __init__(self, volume):
        paths = [ [ [ 1, 1, 0 ],
                    [ 0, 1, 1 ],
                    [ 0, 0, 1 ] ] ]
        super(Kettle, self).__init__(paths, volume)

class HeatExchanger(Component):

    def __init__(self):
        paths = [ [ [ 1, 1, 0, 0 ],
                    [ 1, 1, 0, 0 ],
                    [ 0, 0, 1, 1 ],
                    [ 0, 0, 1, 1 ] ] ]
        super(HeatExchanger, self).__init__(paths)

class WaterInput(StorageComponent):

    def __init__(self):
        paths = [ [ [ 1 ] ] ]
        super(WaterInput, self).__init__(paths)

class Drain(StorageComponent):

    def __init__(self):
        paths = [ [ [ 1 ] ] ]
        super(Drain, self).__init__(paths)

class Sparger(Component):

    def __init__(self):
        paths = [ [ [ 1, 1 ],
                    [ 1, 1 ] ] ]
        super(Sparger, self).__init__(paths)

class Fermenter(StorageComponent):

    def __init__(self):
        paths = [ [ [ 1 ] ] ]
        super(Fermenter, self).__init__(paths)

def generateAdjacencyMatrix():
    global total_num_ports
    global total_num_states

    adj = zeros((total_num_ports, total_num_ports))

    for component in components:
        base_port_id = component.base_port_id
        num_ports = component.num_ports

        # Insert internal port adjacencies
        adj[base_port_id:base_port_id + num_ports,base_port_id:base_port_id+num_ports] += component.paths[0]

        # Insert inter-component port adjacencies
        for portid in range(num_ports):
            for subcomponent, remoteport in component.ports[portid]:
                adj[base_port_id + portid, subcomponent.base_port_id + remoteport] += 1

    return adj

def generatePaths(limit):

    adj = generateAdjacencyMatrix()
    path = adj

    for i in range(limit):
        adj = adj.dot(adj)
        path += adj

    return path

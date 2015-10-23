
    def __init__(self, pathin, pathout, state=0):
        pathin.__add_liquid_input__(self, pathout, state)
        pathout.__add_liquid_output__(self, pathin, state)

class LiquidBiPath(object):

    def __init__(self, path1, path2, state=0):
        self.path1 = LiquidPath(path1, path2, state)
        self.path2 = LiquidPath(path2, path1, state)

# Base Objects
class Component(object):

    def get_interface_components(self):
        return {}

    def get_components(self):
        return []

    def get_state(self):
        return {}

class CType:

    Rate   = 0
    Volume = 1

class Direction:

    Input         = 1
    Output        = 2
    Bidirectional = 3

class ContentType:

    Empty = pow(2,0)
    Sanitiser = pow(2,1)
    Water = pow(2,2)
    Grains = pow(2,3)
    Adjuncts = pow(2,4)
    Wort = pow(2,5)
    Grist = pow(2,6)
    Hops = pow(2,7)
    HoppedWort = pow(2,8)
    SpentHops = pow(2,9)

    LiquidTypes = (Sanitiser & Water & Wort & HoppedWort)
    SolidTypes = (Grains & Adjuncts & Grist & SpentHops)

class LiquidComponent(Component):

    def __init__(self, name, *args, **kwargs):
        self.name = name

class LiquidPort(LiquidComponent):

    def __init__(self,
                 rate=float("inf"),
                 *args, **kwargs):
        self.rate = rate
        super(LiquidPort, self).__init__(*args, **kwargs):
        self.outputs = {}

    def get_state(self, state):
        return { (CType.Rate, self.name) : (self.rate, self.rate) }

    def add_output(self, port, state):
        if not self.outputs.has_key(state):
            self.outputs[state] = set()
        self.outputs[state].add(port)

    def get_external_outputs(self, port, state):
        if not self.ext_outputs.has_key(state):
            self.ext_outputs[state] = set()
        self.ext_outputs[state].add(port)

    # TODO: Add an output list adder and getter
    # Then add in get_rate
    # Then add in get_volume
    # Then add in get_path(other_port)
    # Maybe also/instead get_internal_paths

    def get_rate(self, state):
        rate = 0
        for output in self.outputs[state]:
            rate += output.get_rate(state)
        return min(rate, self.rate)

    def get_internal_paths(self, state, ports):
        if not self.outputs.has_key(state):
            return []

        current_ports = set(self.outputs[state])
        considered_ports = set()

        considered_ports.add(self)
        while len(current_ports):
            port = current_ports.pop()
            considered_ports.add(port)
            current_ports.update(p for p in port.outputs[state] if p not in considered_ports)

        return considered_ports.intersection(ports)

class LiquidVolume(LiquidPort):

    def __init__(self,
                 max_volume=float("inf"),
                 volume_used=0,
                 *args, **kwargs):
        self.max_volume
        self.volume_used = volume_used
        super(LiquidVolume, self).__init__(*args, **kwargs)

    def get_state(self):
        return { (CType.LiquidVolume, self.name) : self.max_volume - self.volume_used
                 }.update(super(LiquidVolume), self).get_state()

def ValveTwoWay(LiquidComponent):

    def __init__(self, *args, **kwargs):
        self.ports = [ LiquidPort(name="Port1", *args, **kwargs),
                       LiquidPort(name="Port2", *args, **kwargs) ]

        self.ports[0].add_output(self.ports[1], 1)
        self.ports[1].add_output(self.ports[0]), 1)
        super(ValveTwoWay, self).__init__(*args, **kwargs)

    def get_state(self):
        valve_states = [ (self.ports, 2) ]
        state_groups = { "valve" : valve_states }

        return state_groups

def ValveThreeWay(LiquidComponent):

    def __init__(self, *args, **kwargs):
        self.switchable_ports = [ LiquidPort(name="Port1", *args, **kwargs),
                                  LiquidPort(name="Port2", *args, **kwargs) ]
        self.common_port = LiquidPort(name="PortCommon", *args, **kwargs)

        self.common_port.add_output(self.switchable_ports[0], 0)
        self.switchable_ports[0].add_output(self.common_port, 0)
        self.common_port.add_output(self.switchable_ports[1], 1)
        self.switchable_ports[1].add_output(self.common_port, 1)

    def get_state(self):
        valve_states = ([self.common_port] + self.switchable_ports, 2)
        state_groups = { "valve" : valve_states }

        return state_groups

# What state is it that you need to represent?
#
# Paths available between Ports (Bi-Directional / One-Way)
# External Ports
# Flow rate available
# Volume Available
# Volume Contents Type
# Switchable Things

for each group of states:
    for each state:
        for each path available:
            list visible ports
            possible flow rate at each port
            possible volume in the path
            think in terms of path direction
            a path is only one input port and one output port,
            but at each port there may be multiple paths in or out,
            (when thinking about rate we only care about the out points at each port)
            (because each visible port of the path is considered individually, all possible routes will be considered)
            going from a (to c) will give a rate and possibly a volume
            going from b (to c) will give a diff rate and volume
            going from c may hit a block, or go to only one of a or b, unlikely both in this example
            start at the input, and follow all other possible paths out, summing/minning as necesary

    def __init__(self, num_states=1, state=0, rate=float("inf")):
        self.state = state
        self.num_states = num_states
        self.liquid_inputs = [ set() for _ in range(num_states) ]
        self.liquid_outputs = [ set() for _ in range(num_states) ]
        self.rate = rate
        super(LiquidComponent, self).__init__()

    def __add_liquid_input__(self, component, state):
        self.liquid_inputs[state].add(component)

    def __add_liquid_output__(self, component, state):
        self.liquid_outputs[state].add(component)

    def get_available_flow_rate(self):
        rate_in = self.rate
        rates_out = [ output.get_available_flow_rate()
                    for output in self.liquid_outputs[self.state] ]
        num_rates_out = len(rates_out)
        total_rate_out = sum(rates_out)

        if total_rate_out > rate_in and num_rates_out > 1:
            warn("Cannot fulfill demand at a split")

        return min(total_rate_in, total_rate_out)

#    def supply(self, available):
#        available = min(available, self.rate)
#        remaining = available
#
#        for output in self.liquid_outputs[self.state]:
#            remaining -= output.supply(remaining)
#
#        return available - remaining

class LiquidConnector(LiquidComponent):
    pass

class LiquidPort(LiquidComponent):
    pass

class ManualLiquidPort(LiquidPort):
    pass

class LiquidVolume(LiquidComponent):
# Switch Everything to kwargs!
# You were in the middle of making receive and release
# They're meant to return how much they take, or how much they give
# If it involves a volume then the ratein/rateout/actualvolume must be taken into account
# Then loop through devices based on stae
# You need state to be stored at the part level somehow?
    def __init__(self,
                 volume,
                 input_rate=float("inf"),
                 output_rate=float("inf"),
                 initial_quantity=0,
                 overflow=false,
                 *args, **kwargs):
        self.volume = volume
        self.input_rate = input_rate
        self.output_rate = output_rate
        self.quantity = initial_quantity
        self.overflow = overflow
        super(LiquidVolume, self).__init__(*args, **kwargs)

    def get_available_volume(self):
        return self.volume - self.quantity

    def get_possible_flow_rate(self):
        if self.overflow:
            return self.input_rate

        # if we can't overflow then we can only put in as much as the pot can take, 
        # plus the amount that will be leaving too
        # unless the input_rate is lower

        available = self.volume - self.quantity
        for output in self.liquid_outputs:
            available += output.get_possible_flow_rate())

        return available

# Demand is the right word, supply is the wrong
# How about demand, consume and supply

# Supply is how much it supplies to the rest per timestep
# Maybe keep track of how much has supplied and
# consumed per timestep so can loop until stable?

# To convert to args and kwargs, introduce __component_init__(*args, *kwargs)
# Call it from Component.__init___
# Does this open up the requirement of __liquid_component_init__ etc?
# 
class Heater(Component):
    pass

class Thermometer(Component):
    pass

# Complex Objects
class Part(object):

    def __init__(self):
        self.ports = []
        self.volumes = []

class Kettle(Part):

    def __init__(self, volume):
        self.inputPort = LiquidPort()
        self.outputPort = LiquidPort()
        self.manualPort = ManualLiquidPort()
        self.ports = [ self.inputPort, self.outputPort, self.manualPort ]
        self.volumes = [ LiquidVolume(volume, true) ]

        LiquidBiPath(self.manualPort, self.volume)
        LiquidPath(self.inputPort, self.volume)
        LiquidPath(self.volume, self.outputPort)

        super(Kettle, self).__init__()

class BallValve2Way(Part):

    def __init__(self):
        self.states = 2
        self.ports = [ LiquidPort(states), LiquidPort(states) ]

        LiquidBiPath(self.ports[0], self.ports[1], 1)

        super(BallValve2Way, self).__init__()

class BallValve3Way(Part):

    def __init__(self):
        self.states = 2
        self.central_port = LiquidPort(self.states)
        self.switchable_ports = [ LiquidPort(self.states). LiquidPort(self.states) ]
        self.ports = [ self.central_port ] + self.switchable_ports

        LiquidBiPath(self.central_port, self.switchable_ports[0], 0)
        LiquidBiPath(self.central_port, self.switchable_ports[1], 1)

        super(BallValve3Way, self).__init__()

class Pump(Part):

    def __init__(self):
        self.states = 2
        self.input_port = LiquidPort(self.states)
        self.output_port = LiquidPort(self.states)
        self.ports = [ self.input_port, self.output_port ]

        LiquidPath(self.input_port, self.output_port, 1)

        super(Pump, self).__init__()

class HeatExchanger(Part):

    def __init__(self):
        self.heater = [ LiquidPort(), LiquidPort() ]
        self.heatee = [ LiquidPort(), LiquidPort() ]
        self.ports = self.heater + self.heatee

        LiquidBiPath(self.heater[0], self.heater[1])
        LiquidBiPath(self.heatee[0], self.heatee[1])

        super(HeatExchanger, self).__init__()

class WaterInput(Part):

    def __init__(self):
        self.output_port = LiquidPort(self.states)
        self.volume = Volume(float("inf"))
        self.ports = [ self.output_port ]
        self.volumes = [ self.volume ]

        LiquidPath(self.output_port, self.volumes[0])

        super(WaterInput, self).__init__()

class Drain(Part):

    def __init__(self):
        self.input_port = LiquidPort(self.states)
        self.ports = [ self.input_port ]

        super(Drain, self).__init__()

class Sparger(Part):

    def __init__(self):
        self.ports = [ LiquidPort(), LiquidPort() ]

        LiquidPath(self.ports[0], self.ports[1])
        LiquidPath(self.ports[1], self.ports[0])

        super(Sparger, self).__init__()

class Fermenter(Part):

    def __init__(self, volume):
        self.ports = [ LiquidPort() ]
        self.volume = Volume(volume, true)
        self.elements = [ self.volume ]

        LiquidPath(self.ports[0], self.volume)

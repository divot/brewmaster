import valves
import gpio

bus = gpio.PCF8574(0x20)

vs = [
    valves.TwoWayValveMISOLTwoWire(
        bus.get_gpio(0, True),
        bus.get_gpio(1, True)
    ),

    valves.TwoWayValveMISOLTwoWire(
        bus.get_gpio(2, True),
        bus.get_gpio(3, True)
    ),

    valves.TwoWayValveMISOLTwoWire(
        bus.get_gpio(4, True),
        bus.get_gpio(5, True)
    ),

    valves.TwoWayValveMISOLTwoWire(
        bus.get_gpio(6, True),
        bus.get_gpio(7, True)
    )
]

for v in vs:
    v.open()

for v in vs:
    v.wait_for_state()

for v in vs:
    v.close()

for v in vs:
    v.wait_for_state()

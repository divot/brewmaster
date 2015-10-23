import container
import numpy

# Main Inputs/Outputs
waterInput = container.WaterInput()
drain = container.Drain()

# Kettles
waterHeater = container.Kettle(100)
mashTun = container.Kettle(100)
hotLiquorTank = container.Kettle(100)

# Special Devices
heatExchanger = container.HeatExchanger()
sparger = container.Sparger()
fermenter = container.Fermenter()

# Pumps
heatLoopPump = container.Pump()
wortLoopPump = container.Pump()

# Valves
waterValve = container.BallValve2Way()

heatLoopMainValve = container.BallValve2Way()
heatLoopDrainValve = container.BallValve3Way()

wortLoopWaterValve = container.BallValve2Way()
wortLoopTunValve = container.BallValve3Way()
wortLoopHLTValve = container.BallValve3Way()
wortLoopDrainValve = container.BallValve3Way()

wortLoopFermenterValve = container.BallValve3Way()
wortLoopHLTInputValve = container.BallValve3Way()
wortLoopTunInputValve = container.BallValve3Way()

# Input  Connections
waterValve.connect(0, 0, waterInput)
waterValve.connect(1, 0, waterHeater)

# Heater Loop Connections
heatLoopMainValve.connect(0, 1, waterHeater)
heatLoopMainValve.connect(1, 0, heatLoopPump)

heatLoopPump.connect(1, 0, heatExchanger)
heatLoopDrainValve.connect(0, 1, heatExchanger)
heatLoopDrainValve.connect(1, 0, drain)
heatLoopDrainValve.connect(2, 0, waterHeater)

# Wort Loop Connections
wortLoopWaterValve.connect(0, 1, waterHeater)
wortLoopWaterValve.connect(1, 1, wortLoopTunValve)

wortLoopTunValve.connect(2, 1, mashTun)

wortLoopHLTValve.connect(0, 0, wortLoopPump)
wortLoopHLTValve.connect(1, 0, wortLoopTunValve)
wortLoopHLTValve.connect(2, 1, hotLiquorTank)

wortLoopDrainValve.connect(0, 1, wortLoopPump)
wortLoopDrainValve.connect(1, 0, drain)
wortLoopDrainValve.connect(2, 2, heatExchanger)

wortLoopFermenterValve.connect(0, 3, heatExchanger)
wortLoopFermenterValve.connect(1, 0, wortLoopHLTInputValve)
wortLoopFermenterValve.connect(2, 0, fermenter)

wortLoopHLTInputValve.connect(1, 0, hotLiquorTank)
wortLoopHLTInputValve.connect(2, 0, wortLoopTunInputValve)

wortLoopTunInputValve.connect(1, 0, mashTun)
wortLoopTunInputValve.connect(2, 0, sparger)

sparger.connect(1, 0, mashTun)

numpy.set_printoptions(threshold=numpy.nan, linewidth=numpy.nan)

print container.generateAdjacencyMatrix() * 10
print container.generatePaths(1) * 10

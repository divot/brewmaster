from kettles import Kettle
from valves import TwoWayValve, ThreeWayValve

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

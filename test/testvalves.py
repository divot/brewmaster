import sys
import os

sys.path.append(os.path.relpath("../src/"))

import RPi.GPIO as GPIO
import time
import valves

GPIO.setmode(GPIO.BCM)

v = valves.TwoWayValveMISOLTwoWire(24,25)
v.open()
time.sleep(5)
v.close()
time.sleep(5)

GPIO.cleanup()

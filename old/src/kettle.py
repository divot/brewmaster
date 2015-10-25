from switch import Switch

class Kettle(object):

    def __init__(self, therm = None, devices = None):
        self.therm = therm
        self.devices = devices

    def has_therm(self):
        return bool(self.therm)

    def has_switchable_heater(self):
        raise NotImplementedError

    def can_set_temp(self):
        return self.has_therm() and self.has_switchable_heater()

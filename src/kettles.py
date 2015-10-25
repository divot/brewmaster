from liquidcomponent import LiquidComponent

class Kettle(LiquidComponent):

    DEFAULT_NAME = "Kettle"

    def __init__(self, name=DEFAULT_NAME):
        super(Kettle, self).__init__(name)

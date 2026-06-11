from abstract_classes import monster


class sparkie(monster):
    """A high damage low health monster."""
    def __init__(self):
        super().__init__(name="sparkie", damage=25, max_health=80)
        print("sparkieiinstantiated")

class hydragon(monster):
    """A low damage high health monster."""
    def __init__(self):
        super().__init__(name="hydragon", damage=15, max_health=120)
        print("hydragon at your service")

class ember(monster):
    """An all rounder monster."""
    def __init__(self):
        super().__init__(name="ember", damage=20, max_health=100)
        print("ember here about to make things hot")
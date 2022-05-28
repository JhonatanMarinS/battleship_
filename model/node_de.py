from .ship_distribution import ShipDistribution

class NodeDe:
    def __init__(self, data:ShipDistribution):
        self.data = data
        self.next = None
        self.previous = None

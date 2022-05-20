from .ship import Ship


class ShipDistribution:
    def __init__(self, ship: Ship):
        self.places = []
        self.ship = Ship
        self.orientation = 0
        self.state = "FREE"

    def ship_distribution(self, data, ship: Ship):
        self.places =[Ship(data.num_places)]



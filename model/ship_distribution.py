from .ship import Ship

class ShipDistribution:

    def __init__(self, ship:Ship):
        self.places = []
        self.ship = Ship
        self.orientation = 0
        self.state = "FREE"
        self.sunken_ship = 0

    def validate_shoot(self, x: int, y: int):
        for coordinate in self.places:
            if x == coordinate.x and y == coordinate.y:
                self.places.state = True
                return True
            else:
                return False

    def validate_location(self):
        num_places = self.ship.num_places
        return num_places

    def sunken_ships(self):
        count = 0
        num_places = self.ship.num_places

        for i in self.places:
            if self.places.state == True:
                count += 1
        if count == num_places:
            self.sunken_ship += 1
            return self.sunken_ship

    def define_location(self, x: int, y: int):
        num_places = self.ship.num_places



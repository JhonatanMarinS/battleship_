from .user import User
from .list_de import ListDe
from .ship_distribution import ShipDistribution


class Board:

    def __init__(self, rows: int, columns:int, player: User, ship_list:ListDe, id:int):
        self.id = id
        self.columns = columns
        self.rows = rows
        self.ship_list = ship_list
        self.player = player
        self.State_board = False
        self.received_shoots = []

    def validate_shoot(self, x:int, y:int):
        if x < self.rows and y < self.columns:
            for receivedShoots in self.received_shoots:
                if x == receivedShoots.x and y == receivedShoots.y:
                    raise Exception("Este punto ya ha sido atacado")
                else:
                    if ShipDistribution.validate_shoot(x, y):
                        self.received_shoots.append(x, y)
                        return ("toco un barco")
                    else:
                        self.received_shoots.append(x, y)
                        return ("toco agua")
        else:
            raise Exception("Esta coordenada no es valida")


    def validate_location(self, type:int):
        num_places = ShipDistribution.validate_location()
        if type == 1:
            for i in num_places:
                if self.rows.x != None:
                    break
            return True

        if type == 2:
            for i in num_places:
                if self.columns.y != None:
                    break
            return True

    def define_location(self, x:int, y:int, orientation:int):
        if x < self.rows and y < self.columns:
            if orientation == 0:
                if self.rows.y == None:
                    self.rows.y = y
                    if self.validate_location(2):
                        num_places = ShipDistribution.validate_location()
                        for i in num_places:
                            self.columns.y = y
            else:
                raise Exception ("No es posible ubicarlo desde el eje y")

            if orientation == 1:
                if self.columns.x == None:
                    self.columns = x
                    if self.validate_location(1):
                        num_places = ShipDistribution.validate_location()
                        for i in num_places:
                            self.rows.x = x
            else:
                raise Exception ("No es posible ubicarlo desde el eje x")


    def validate_winner(self):
        num_ships = ShipDistribution.sunken_ships()


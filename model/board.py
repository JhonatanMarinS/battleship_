from .user import User
from .list_de import ListDe

class Board:

    def __init__(self, rows: int, columns:int, player: User, ship_list:ListDe, id: int):
        self.id = id
        self.columns = columns
        self.rows = rows
        self.ship_list = ship_list
        self.player = player
        self.State_board = False
        self.received_shots = []

    def validate_shoot(self, data, ):
        pass

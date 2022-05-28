from .user import User
from .list_de import ListDe
from .board import Board


class Game:
    def __init__(self, player_1:User,player_2:User, ship_list:ListDe, id:int):
        self.id = id
        self.player_1 = player_1
        self.player_2 = player_2
        self.num_ships = ship_list.count
        self.ship_list = ListDe
        self.turn = 0
        self.hits_player_1 = 0
        self.hits_player_2 = 0
        self.board_player_1 = None
        self.board_player_2 = None
        self.__create_board(ship_list)

    def __create_board(self, ship_list:ListDe):
        size = 0
        if self.num_ships < 10:
            size = 10

        elif self.num_ships < 20:
            size = 20

        else:
            size = 30

        self.board_player_1 = Board(1,size,size,self.player_1, ship_list)
        self.board_player_2 = Board(2, size, size, self.player_2, ship_list.clone_list())


    def validate_shoot(self, x:int, y:int, player:User):
        if player == self.player_1:
            board = self.board_player_2
            board.validateShoots(x, y)

        elif player == self.player_2:
            board = self.board_player_1
            board.validateShoots(x, y)

    def define_location(self, x:int, y:int, player:User, orientation: int):
        if player == self.player_1:
            board = self.board_player_1
            board.define_location(x, y, orientation)

        elif player == self.player_2:
            board = self.board_player_2
            board.define_location(x, y, orientation)

    def validate_winner(self):
        sunken_ships_1 = self.board_player_1.validate_winner()
        sunken_ships_2 = self.board_player_2.validate_winner()

        if self.num_ships == sunken_ships_1:
            return ("El jugador 1 ha ganado el juego")

        if self.num_ships == sunken_ships_2:
            return ("El jugador 2 ha ganado el juego")

        else:
            raise Exception ("Ningun jugador ha ganado")


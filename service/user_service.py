from model.user import User
from model.type_user import TypeUser
from model.game import Game


import random

class UserService:

    def __init__(self):
        self.admin = None
        self.player_1 = None
        self.player_2 = None

    def create_user(self, data):
        count_player = 0
        count_admin = 1
        type_user = data['type_user']

        if self.validate_email():

            if type_user == 1 and count_admin == 1:
                self.admin = User(data, 1, TypeUser(1, "Administrador"))
                count_admin += 1

            elif type_user == 1 and count_admin > 1:
                raise Exception("Ya hay un administrador registrado")

            if type_user == 2 and count_player == 0:
                self.player_1 = User(data, 2, TypeUser(2, "Jugador"))
                count_player += 1

            if type_user == 2 and count_player == 1:
                self.player_2 = User(data, 3, TypeUser(2, "Jugador"))
                count_player += 1

            elif type_user == 2 and count_player > 2:
                raise Exception("Ya hay dos jugadores registrados")

            else:
                raise Exception("tipo de usuario invalido")
        else:
            raise Exception("Este correo ya ha sido registrado")

    def validate_email(self, data):
        list = self.read_users()
        email = data['email']
        for user in list:
            if user.email == email:
                return False
        return True

    def login(self, data):
        for user in self.userList:
            if data['email'] == user.email and data['password'] == user.password:
                return user
        return None

    def read_users(self):
        list = []

        if self.admin != None:
            list.append(self.admin.toDTO)

        if self.player_1 != None:
            list.append(self.player_1.toDTO)

        if self.player_2 != None:
            list.append(self.player_2.toDTO)

        return list

    def delete_user(self, data):

        email= data["email"]
        if email == self.admin.email:
            raise Exception("No es posible eliminar el administrador")

        elif email == self.player_1.email:
            self.player_1 = None
            self.count_player -= 1

        elif email == self.player_2.email:
            self.player_2 = None
            self.count_player -= 1

        else:
            raise Exception("No se ha encontrado ningun usuario")

    def define_location(self, x:int, y:int, orientation:int):
        Game.define_location(x, y, orientation)


    def define_location(self, x:int, y:int, player:User):
        Game.validate_shoot(x, y, player)



    def move_jp1(self):
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.player_1 = random.choice(choices)

    def move_jp2(self,):
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.player_2 = random.choice(choices)

    def game_lift(self):
        self.move_jp1()
        self.move_jp2()

        winmoves = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
             "scissors": ["paper", "lizard"],
             "lizard": ["paper", "spock"],
             "spock": ["scissors", "rock"],
        }

        if self.player_1 == self.player_2:
            return "jp1: "+self.player_1, "jp2: "+self.player_2,"Ha sido un empate"

        elif self.player_2 in winmoves[self.player_1]:
            return "jp1: "+self.player_1, "jp2: "+self.player_2, "Ha ganado el jugador 1"

        else:
            return "jp1: "+self.player_1, "jp2: "+self.player_2, "Ha ganado el jugador 2"


from model.user import User
from model.type_user import TypeUser


class UserService:
    def __init__(self):
        self.admin = None
        self.player_1 = None
        self.player_2 = None

    def create_user(self, data):
        count = 0
        type_user = data['type_user']

        if type_user == 1:
            self.admin = User(data, 1, TypeUser(1, "Administrador"))

        if type_user == 2:
            self.player_1 = User(data, 2, TypeUser(2, "Jugador"))
            count =+1

        if type_user == 2 and count == 1:
            self.player_2 = User(data, 3, TypeUser(2, "Jugador"))

        else:
            raise Exception("tipo de usuario invalido")


    def Read_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):

        pass
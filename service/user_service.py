from model.user import User
from model.type_user import TypeUser
from model.user_dto import UserDTO

class UserService:

    def __init__(self):
        self.admin = None
        self.player_1 = None
        self.player_2 = None

    def create_user(self, data):
        count_player = 0
        count_admin = 1
        type_user = data['type_user']

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

    def validate_email(self, data):
        list = self.read_users()
        email = data['email']
        for user in list:
            if user.email == email:
                raise Exception('Este email ya esta siendo utilizado')


    def login(self):
        pass

    def read_users(self,):
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






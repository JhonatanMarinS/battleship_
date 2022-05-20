from flask import Flask
from controller.list_de_controller import app_list_de
from controller.user_controller import app_user
app = Flask(__name__)
app.register_blueprint(app_list_de)
app.register_blueprint(app_user)
if __name__ == '__main__':
    app.run()

from flask import Response,json,jsonify,Blueprint, request
from service.user_service import UserService
from util.util_encoder import UtilEncoder
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity

app_user = Blueprint("app_user",__name__)

user_service = UserService()

@app_user.route('/user')
def list():
    return Response(status=200, response=json.dumps(user_service.read_users(),
                                                    cls=UtilEncoder), mimetype="application/json")

@app_user.route('/user/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        user = user_service.login(email, password)
        access_token = create_access_token(identity={'user': user})
        return jsonify({'token': access_token})
    except Exception as e:
        return jsonify({'message': str(e)})

@app_user.route('/user/definirubi/<x>/<y>/<orientation>')
def define_location():
    return Response(status=200, response=json.dumps(user_service.define_location(),
                                                    cls=UtilEncoder), mimetype="application/json")

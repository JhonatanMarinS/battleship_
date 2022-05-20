from flask import Response,json,jsonify,Blueprint, request
from service.user_service import User
from util.util_encoder import UtilEncoder

app_user = Blueprint("app_user",__name__)

user_service = User()

@app_user.route('/user')
def Create():

    return Response(status=200, response=json.dumps(user_service.Create_user(),
                                                    cls=UtilEncoder), mimetype="application/json")

from flask import Response,json,jsonify,Blueprint, request
from service.list_de_service import ListDeService
from util.util_encoder import UtilEncoder
from model.ship import Ship


app_list_de = Blueprint("app_list_de",__name__)

list_de_service = ListDeService()

@app_list_de.route('/listDe')
def list():
    return Response(status=200, response=json.dumps(list_de_service.list(),
                                                    cls=UtilEncoder), mimetype="application/json")

@app_list_de.route('/listDe', methods=['POST'])
def create():
    data = request
    list_de_service.add(Ship(data, list_de_service))
    return list_de_service.add(Ship(data, list_de_service.count +1))




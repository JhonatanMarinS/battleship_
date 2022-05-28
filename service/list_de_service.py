from model.list_de import ListDe
from model.ship import Ship
from model.ship_distribution import ShipDistribution


class ListDeService:

    def __init__(self):
        self.list_de = ListDe()

    def list(self):
        return self.list_de.list()

    def add(self,data:Ship):
        ship_dist = ShipDistribution(data)
        self.list_de.add(ship_dist)
        return {"message":"Barco adicionado correctamente"}

    def add_to_star(self,data:Ship):
        ship_dist = ShipDistribution(data)
        self.list_de.add_to_start(ship_dist)
        return {"message":"Barco adicionado correctamente"}

    def clone_list(self):
        return self.list_de.clone_list().list()
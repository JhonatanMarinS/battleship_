from .node_de import NodeDe
from .ship_distribution import ShipDistribution

class ListDe:
    def __init__(self, data):
        self.head = None
        self.count = 0

    def add(self, data:ShipDistribution):
        if self.head == None:
            self.head = NodeDe(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = NodeDe(data)
            temp.next.previous = temp
        self.count =+ 1

    def add_to_start(self, data:ShipDistribution):
        if self.head == None:
            self.head = NodeDe(data)
        else:
            self.head.previous = NodeDe
            self.head.previous.next = self.head
            self.head = self.head.previous
        self.count =+ 1

    def clone_list(self):
        list_clon = ListDe()
        temp = self.head
        while temp.next != None:
            list_clon.add(temp.data)
            temp = temp.next
        return list_clon

    def list(self):
        list = []
        if self.head != None:
            temp = self.head
            while temp.next != None:
                list.append(temp.data)
                temp = temp.next
        else:
            raise Exception("No hay datos que listar")
        return list


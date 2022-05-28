from .node_de import NodeDe
from .ship_distribution import ShipDistribution

class ListDe:
    def __init__(self):
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
        list = ListDe()
        temp = self.head
        while temp != None:
            list.add(temp.data)
            temp = temp.next
        return list

    def list(self):
        list = []
        temp = self.head
        while temp != None:
            list.append(temp.data)
            temp = temp.next
        return list

